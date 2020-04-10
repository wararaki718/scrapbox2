#include <iostream>
#include <string>
#include <vector>
#include <clocale>

using namespace std;

vector<wstring> get_n_gram(wstring str, int n)
{
    vector<wstring> n_grams;
    for(int i = 0; i <= str.size()-n; i+=n){
        n_grams.push_back(str.substr(i, n));
    }
    return n_grams;
}

void show_data(vector<wstring> words)
{
    cout << "show " << words[0].size() << "-gram words" << endl;
    for(auto it = words.begin(); it != words.end(); it++) {
        wcout << *it << endl;
    }
    cout << endl;
}

int main()
{
    wcout.imbue(locale(""));
    wstring s = L"私はご飯を食べます。";
    
    wcout << s << endl;
    cout << s.size() << endl;
    cout << endl;

    show_data(get_n_gram(s, 1));
    show_data(get_n_gram(s, 2));
    show_data(get_n_gram(s, 3));

    return 0;
}
