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


int get_substring_index(string pattern, vector<suffix_string> suffix_array)
{
    for(auto it = suffix_array.begin(); it != suffix_array.end(); it++) {
        string suffix_str = (*it).s;
        if(suffix_str.size() < pattern.size()) {
            continue;
        }

        if(suffix_str.substr(0, pattern.size()) == pattern) {
            return (*it).index;
        }
    }
    // do not find
    return -1;
}


int main()
{
    string s = "hello,world!";
    string pattern = "wor";

    vector<suffix_string> suffix_array;
    for(int i = 0; i < s.size(); i++) {
        suffix_string ss;
        ss.s = s.substr(i);
        ss.index = i;
        suffix_array.push_back(ss);
    }
    sort(suffix_array.begin(), suffix_array.end(), compLess);
    show_suffix_array(suffix_array);

    int index = get_substring_index(pattern, suffix_array);
    cout << "pattern {" << pattern << "}, target {" << s << "}, index {" << index << "}" << endl;

    return 0;
}
