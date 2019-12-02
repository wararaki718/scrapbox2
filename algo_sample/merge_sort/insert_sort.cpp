#include <iostream>
#include <vector>

using namespace std;


void show(vector<int> vec)
{
    for(auto it = vec.begin(); it != vec.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
}


void insert_sort(vector<int>::iterator begin, vector<int>::iterator end)
{
    for(auto it = begin; it != end; it++) {
        int key = *it;
        auto i = it - 1;
        while(i != begin-1 && *i > key) {
            *(i+1) = *i;
            i--;
        }
        *(i+1) = key;
    }
}


int main()
{
    vector<int> vec{5, 7, 8, 3, 6, 10, 1, 2};
    show(vec);
    insert_sort(vec.begin(), vec.end());
    show(vec);
    return 0;
}