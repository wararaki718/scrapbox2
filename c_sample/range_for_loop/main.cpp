#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v({1, 2, 3, 4, 5, 6});
    for(const auto& e : v) {
        cout << e << endl;
    }
    return 0;
}