#include <iostream>
#include <climits>
#include <algorithm>

using namespace std;

int main()
{
    int a[] = {5, 2, -1, 0, 3};
    int window_size = 3;
    int n = sizeof(a)/sizeof(a[0]);

    int max_sum = INT_MIN;
    int current_sum;
    for(auto i = 0; i < n-window_size; i++) {
        current_sum = 0;
        for(auto j = i; j < window_size; j++) {
            current_sum += a[j];
        }
        
        max_sum = max(max_sum, current_sum);
    }

    cout << max_sum << endl;
    return 0;
}