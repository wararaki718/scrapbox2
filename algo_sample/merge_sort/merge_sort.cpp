#include <iostream>
#include <vector>
#include <climits>

using namespace std;


void show(vector<int> vec)
{
    for(auto it = vec.begin(); it != vec.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;
}


void merge(vector<int> *ary, int left, int mid, int right)
{
    int n = mid - left;
    int m = right - mid;

    vector<int> lary;
    vector<int> rary;

    for(int i = 0; i < n; i++)
        lary.push_back((*ary)[left+i]);

    for(int i = 0; i < m; i++)
        rary.push_back((*ary)[mid+i]);

    lary.push_back(INT_MAX);
    rary.push_back(INT_MAX);

    int i = 0, j = 0;
    for(int k = left; k < right; k++) {
        if(lary[i] <= rary[j]) {
            (*ary)[k] = lary[i];
            i++;
        } else {
            (*ary)[k] = rary[j];
            j++;
        }
    }
}


void merge_sort(vector<int> *ary, int left, int right)
{
    if(left + 1 < right) {
        int mid = (left+right)/2;
        merge_sort(ary, left, mid);
        merge_sort(ary, mid, right);
        merge(ary, left, mid, right);
    }
}


int main()
{
    vector<int> vec{5, 7, 8, 3, 6, 10, 1, 2};
    show(vec);
    merge_sort(&vec, 0, vec.size());
    show(vec);
    return 0;
}