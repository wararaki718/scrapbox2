#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


vector<int> make_divisor(int n) {
    vector<int> divisors;

    for(auto i = 1, l = (int)(sqrt(n))+1; i < l; i++) {
        if(n%i == 0) {
            divisors.push_back(i);
            if(i!=((int)(n/i))) {
                divisors.push_back((int)(n/i));
            }
        }
    }

    return divisors;
}


int main()
{
    int n;
    cin >> n;

    auto divisors = make_divisor(n);
    sort(divisors.begin(), divisors.end());

    for(auto divisor : divisors) {
        cout << divisor << endl;
    }

    return 0;
}
