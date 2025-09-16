
#include<bits/stdc++.h>
using namespace std ;

int main()
{
    // INPUT-01) TESTCASE
    int T ;
    cin >> T ;
    
    while(T--){
        string S ;
        string T ;
        
        cin >> S >> T ; 
        
        string result = "" ;
        for(int i=0 ; i<S.size() ; i++){
            
            if(S[i] == T[i]){
                result += 'G' ;
            }
            else{
                result += 'B' ;
            }
            // END OF FOR LOOP
        }
        
        cout<< result << endl ;
    }
    return 0 ;
}
