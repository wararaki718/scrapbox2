#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;


struct suffix_string {
    string s;
    int index;
};


struct suffix_comp {
    bool operator()(const suffix_string s1, const suffix_string s2) const {
        return s1.s < s2.s;
    }
} compLess;


void show_suffix_array(vector<suffix_string> suffix_array)
{
    for(auto it = suffix_array.begin(); it != suffix_array.end(); it++) {
        cout << (*it).index << ":" << (*it).s << endl;
    }
    cout << endl;
}


int binary_search(string pattern, vector<suffix_string> suffix_array)
{
    int low = 0;
    int high = suffix_array.size() - 1;
    while (low <= high) {
        int mid = (high + low)/2;
        suffix_string suffix_item = suffix_array[mid];

        if(suffix_item.s.size() >= pattern.size() &&
           suffix_item.s.substr(0, pattern.size()) == pattern) {
            return suffix_item.index;
        }

        if(suffix_item.s > pattern) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    // not find
    return -1;
}


int main()
{
    string s = "hello,world!";
    string pattern = "wor";

    vector<suffix_string> suffix_array;
    for(int i = 0; i < s.size(); i++) {
        suffix_array.push_back({s.substr(i), i});
    }
    sort(suffix_array.begin(), suffix_array.end(), compLess);
    show_suffix_array(suffix_array);

    // search
    int index = binary_search(pattern, suffix_array);
    cout << "pattern {" << pattern << "}, target {" << s << "}, index {" << index << "}" << endl;

    return 0;
}
