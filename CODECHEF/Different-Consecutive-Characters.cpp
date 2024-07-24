#include<bits/stdc++.h>

using namespace std;

int main() {

    int T; //TESTCASE
    cin >> T;


    while (T--) {

        int N;
        string S;

        cin >> N >> S;

        int operationCount = 0;

        for (int i = 0; i < S.size(); i++) {
            if (S[i] == S[i + 1]) {
                operationCount++;
            }
        }

        cout << operationCount << endl ;
    }

    return 0;
}
