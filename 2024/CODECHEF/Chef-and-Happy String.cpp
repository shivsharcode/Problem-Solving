#include <bits/stdc++.h>
using namespace std;

bool is_vowel(char c){
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ;
}

int main() {
    // your code goes here
    int T;
    cin >> T;
    while (T--) {

        string S;
        cin >> S;

        string result = "Sad";

        for (int i = 0; i < S.size() - 2; i++) {
            char first = S[i];
            char second = S[i + 1];
            char third = S[i + 2];

            if (is_vowel(first) && is_vowel(second) && is_vowel(third)
            ) {
                result = "Happy";
                break;
            }
        }

        cout << result << endl;
    }
    return 0 ;
}
