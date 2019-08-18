#include <iostream>
#include <cmath>

using namespace std;

int get_digit(int val)
{
    return (int)log10(val) + 1;
}

int main()
{
    int samples[] = {1, 20, 321, 2345};
    for(auto val: samples){
        cout << val << ": " << get_digit(val) << endl;
    }
    return 0;
}