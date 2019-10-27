import React from 'react';
import './App.css';
import axios from 'axios';

interface Props {}

interface State {
  value: string;
  status: string;
  username: string;
  location: string;
  created_at: string;
}

class App extends React.PureComponent<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      value: '',
      status: '',
      username: '',
      location: '',
      created_at: ''
    };

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    const self = this;
    axios.get('https://api.github.com/users/wararaki')
      .then(response => {
        self.setState({
          value: String(Date.now()),
          status: String(response.status),
          username: response.data.login,
          location: response.data.location,
          created_at: response.data.created_at
        });
      });
  }
  
  render() {
    return (
      <div>
        <div>
          <button onClick={this.handleClick}>
            click
          </button>
        </div>
        <div>
          Status: {this.state.status}
        </div>
        <div>
          AccessTime: {this.state.value}
        </div>
        <div>
          Username: {this.state.username}
        </div>
        <div>
          Location: {this.state.location}
        </div>
        <div>
          CreatedAt: {this.state.created_at}
        </div>
      </div>
    );
  }
}

export default App;