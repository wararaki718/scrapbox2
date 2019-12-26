#include <iostream>
#include <typeinfo>

using namespace std;

template<typename T>
T add(T a, T b) {
    return a + b;
}

template<typename T>
void show(T a) {
    T aa = add(a, a);
    cout << aa << " : " << typeid(aa).name() << endl;
}

int main()
{
    int a = 1;
    float b = 2.0;
    double c = 3.0;
    
    show(a);
    show(b);
    show(c);

    return 0;
}