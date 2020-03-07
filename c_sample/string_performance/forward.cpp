#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s = "";
    for(int i = 0; i < 1000000; i++) {
        s = "a" + s;
    }
    cout << "DONE" << endl;
    return 0;
}