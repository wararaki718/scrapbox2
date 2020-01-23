#include <iostream>
#include <algorithm>

#define MAX_N 100
#define MAX_W 10000

using namespace std;

int main()
{
    int N, W;
    cin >> N >> W;
    int v[MAX_N];
    int w[MAX_N];

    for(int i = 0; i < N; i++) {
        cin >> v[i] >> w[i];
    }

    int dp[MAX_N+1][MAX_W+1];
    for(int i = 0; i <= MAX_W; i++) {
        dp[0][i] = 0;
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j <= W; j++) {
            if(j >= w[i]) {
                dp[i+1][j] = max(dp[i][j-w[i]]+v[i], dp[i][j]);
            } else {
                dp[i+1][j] = dp[i][j];
            }
        }
    }
    cout << dp[N][W] << endl;

    return 0;
}
