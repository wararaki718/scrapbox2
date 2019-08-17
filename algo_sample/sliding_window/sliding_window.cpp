#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int a[] = {5, 2, -1, 0, 3};
    int window_size = 3;
    int n = sizeof(a)/sizeof(a[0]);

    int max_sum = 0;
    for(auto i = 0; i < window_size; i++) {
        max_sum += a[i];
    }

    int window_sum = max_sum;
    for(auto i = window_sum; i < n; i++) {
        window_sum += (a[i]-a[i-window_sum]);
        max_sum = max(max_sum, window_sum);
    }

    cout << max_sum << endl;
    return 0;
}