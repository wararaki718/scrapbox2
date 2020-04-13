import numpy as np
import pandas as pd


def viterbi(p_i: np.array,
            hmm_states: np.array,
            obs_states: np.array,
            data: np.array):
    
    n_obs_states = obs_states.shape[0]
    n_time = data.shape[0]

    path = np.zeros(n_time, dtype=int)
    delta = np.zeros((n_obs_states, n_time))
    phi = np.zeros((n_obs_states, n_time))

    delta[:, 0] = p_i * obs_states[:, data[0]]
    phi[:, 0] = 0

    # forward algorithm
    for t in range(1, n_time):
        for s in range(n_obs_states):
            delta[s, t] = np.max(delta[:, t-1] * hmm_states[:, s]) * obs_states[s, data[t]]
            phi[s, t] = np.argmax(delta[:, t-1] * hmm_states[:, s])

    # find optimal path
    path[n_time-1] = np.argmax(delta[:, n_time-1])
    for t in range(n_time-1, 0, -1):
        path[t-1] = phi[path[t], t]
    
    return path, delta, phi


def main():
    obs_map = {
        'Cold': 0,
        'Hot': 1
    }
    obs = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1])

    inv_obs_map = {
        value: key for key, value in obs_map.items()
    }
    obs_seq = [inv_obs_map[value] for value in obs]

    print('simulated observations:')
    print(pd.DataFrame(np.column_stack([obs, obs_seq]), columns=['obs_code', 'obs_seq']))
    print()

    # p_i = [0.6, 0.4]
    states = list(obs_map.keys())
    hidden_states = ['Snow', 'Rain', 'Sunny']
    p_i = np.array([0.0, 0.2, 0.8])

    # state_space = pd.Series(p_i, index=hidden_states, name='states')
    hmm_df = pd.DataFrame([
        [0.3, 0.3, 0.4],
        [0.1, 0.45, 0.45],
        [0.2, 0.3, 0.5]
    ], index=hidden_states, columns=hidden_states)
    print('HMM matrix:')
    print(hmm_df)
    print()

    observable_states = states
    obs_df = pd.DataFrame([
        [1.0, 0.0],
        [0.8, 0.2],
        [0.3, 0.7]
    ], index=hidden_states, columns=observable_states)
    print('Observable layer matrix:')
    print(obs_df)
    print()

    path, delta, phi = viterbi(p_i, hmm_df.values, obs_df.values, obs)
    state_map = {i: hidden_state for i, hidden_state in enumerate(hidden_states)}
    state_path = [state_map[value] for value in path]
    print(pd.DataFrame().assign(observation=obs_seq).assign(best_path=state_path))
    print()

    print('delta:')
    print(delta)
    print()

    print('phi:')
    print(phi)
    print()

    print('DONE')


if __name__ == '__main__':
    main()
