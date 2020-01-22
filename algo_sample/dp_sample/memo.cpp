#include <iostream>
#include <algorithm>

#define N 1000

using namespace std;

int memo[N];
int fib(int n)
{
    if(n == 0) {
        return 0;
    }
    if(n == 1) {
        return 1;
    }

    if(memo[n] != -1) {
        return memo[n];
    }

    return memo[n] = fib(n-1) + fib(n-2);
}


int main()
{
    int n = 40;

    fill(memo, memo+N, -1);
    cout << fib(n) << endl;

    return 0;
}