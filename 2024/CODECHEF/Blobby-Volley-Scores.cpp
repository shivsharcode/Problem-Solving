#include <bits/stdc++.h>
using namespace std;

string blobbyVolleyScore(string S){
    
    bool Alice_server = true ;
	    int aliceScore = 0 ;
	    int bobScore = 0 ;
	    
	    for(char &i : S){
	        if(Alice_server){
	            if(i == 'A')
	                aliceScore ++ ;
	            else
	                Alice_server = false ;
	        }
	        
	        else{
	            if(i == 'B')
	                bobScore++ ;
	            else
	                Alice_server = true ;
	            
	        }
	       //END OF FOR LOOP 
	    }
	    
	    string result = to_string(aliceScore) + " " + to_string(bobScore) ;
	    
	    return result ;
}

int main() {
	// your code goes here
	int T ;
	cin >> T ;
	while(T--){
	    
	    int numTurns ;
	    cin >> numTurns ;
	    
	    string S ;
	    cin >> S ;
	    
	    string result = blobbyVolleyScore(S) ;
	    cout << result << endl ;
	}
	
    return 0 ;
}
