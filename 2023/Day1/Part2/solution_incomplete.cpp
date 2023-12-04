#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;



int main() {
    map<string,char> translate{{"one",'1'},{"two",'2'},{"three",'3'},{"four",'4'},{"five",'5'},{"six",'6'},{"seven",'7'}, {"eight",'8'}, {"nine",'9'}};
    char get_first(string s) {
    // Iterate over the dictionary
    // find matches?
    // is digits index
    // if isdigit comes before first spelling then return that
        for (auto& [key,value] : translate) {
        int string_len = key.length();
            for (int i = 0;i < s.length() - string_len; i++ ){
                if (substr(i, string_len))
            }
        }
    }
    ifstream file("input.txt");
    string line;
    int total = 0;
    while(getline(file,line)) {
        char firstDigit = '0';
        char lastDigit = '0';
    }
}
