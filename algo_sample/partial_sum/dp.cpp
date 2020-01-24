#include <iostream>
#include <algorithm>
#include <cstring>

#define MAX_N 100
#define MAX_A 10000

using namespace std;


int main()
{
    int n, A;
    cin >> n >> A;

    int a[MAX_A];
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }

    bool dp[MAX_N+1][MAX_A+1];
    memset(dp, false, sizeof(dp));
    dp[0][0] = true;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= A; j++) {
            if(j >= a[i]) {
                dp[i+1][j] = dp[i][j-a[i]] | dp[i][j];
            } else {
                dp[i+1][j] = dp[i][j];
            }
        }
    }

    if(dp[n][A]) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}