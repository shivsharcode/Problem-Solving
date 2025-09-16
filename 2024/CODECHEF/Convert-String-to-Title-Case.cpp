// PYTHON SOLN IS PREFERRED
#include <bits/stdc++.h>

using namespace std;

int main() {
    // your code goes here

    int T;
    cin >> T;
    cin.ignore();

    while (T--) {

        // STRING INPUT
        string s;
        getline(cin, s);

        //SPLIT THE STRING TO WORDS
        vector < string > parts;
        string cum = "";

        for (const auto & i: s) {

            if (i == ' ') {
                parts.push_back(cum);
                cum = "";
            }
            else {
                cum += i;
            }
            // END OF FOR LOOP
        }
        parts.push_back(cum);


        // CONVERSION 
        string result = "";

        for (const auto & word: parts) {
            string upperWord = word; //CREATE A UPPERCASE COPY OF THE WORD
            for (char & c: upperWord) {
                c = toupper(c);
            }

            if (word != upperWord) { // CHECK IF THE WORD IS NOT UPPERCASED
                string lowerWord = word;
                for (char & l: lowerWord) {
                    l = tolower(l);
                }
                lowerWord[0] = toupper(lowerWord[0]);

                result = result + " " + lowerWord;
            }
            else {
                result = result + " " + upperWord;
            }

        }

        cout << result << endl;

    }

    return 0;
}
