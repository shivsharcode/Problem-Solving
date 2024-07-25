// APPROACH HASHMAPS
#include <bits/stdc++.h>
using namespace std;

string addOne(string s, int indx) {
    // hashmap
    map < char, char > m;
    m['0'] = '1';
    m['1'] = '2';
    m['2'] = '3';
    m['3'] = '4';
    m['4'] = '5';
    m['5'] = '6';
    m['6'] = '7';
    m['7'] = '8';
    m['8'] = '9';
    m['9'] = '0';

    char lastNum = s[indx];

    s[indx] = m[lastNum];
    indx--;

    while (lastNum == '9') {
        lastNum = s[indx];
        s[indx--] = m[lastNum];
    }

    // if (lastNum == '9') {//runtime error dega bcoz baari bari map redeclare hoge
    //   s = addOne(s, indx - 1);
    // }
    
    return s;
}

int main() {
    // your code goes here
    int T;
    cin >> T;
    while (T--) {

        string N;
        cin >> N;

        N = '0' + N;

        // add one in last
        int lastIdx = N.size() - 1;
        N = addOne(N, lastIdx);


        if (N[0] == '0') {
            N = N.substr(1, lastIdx);
        }
        cout << N << endl;
    }

    return 0;
}
