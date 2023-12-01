#include <iostream>
#include <fstream>
#include <string> 
#include <cctype>

using namespace std;
int main() {
    ifstream file("input.txt");
    string line;
    int total = 0;

    while (getline(file, line)) {
        char firstDigit = '0';
        char lastDigit = '0';
        bool foundDigit = false;

        // Find the first digit
        for (char c : line) {
            if (isdigit(c)) {
                firstDigit = c;
                foundDigit = true;
                break;
                
            }
        }

        // Find the last digit
        if (foundDigit) {
            // Reversing it
            for (auto it = line.rbegin(); it != line.rend(); ++it) {
                if (isdigit(*it)) {
                    lastDigit = *it;
                    break;
                }
            }
        }

        if (foundDigit) {
            // This is an interesting way to do it rather than doing stoi
            int newDigit = (firstDigit - '0') * 10 + (lastDigit - '0');
            total += newDigit;
        }
    }

    std::cout << total << std::endl;

    return 0;
}