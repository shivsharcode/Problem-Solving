// APPROACH - 1 : USING UNORDERED MAPS
// TIME COMPLEXITY : O(T X N/2)
// SPACE COMP      : O(T X N/2)
#include <bits/stdc++.h>
using namespace std ;

int main() {

  // INPUT-1 ) THE TESTCASES
	int T ;
	cin >> T ;
	
	unordered_map <string, char> m ;
	
	m["00"] = 'A' ;
	m["01"] = 'T' ;
	m["10"] = 'C' ;
	m["11"] = 'G' ;
	
	while(T--){
	    int inputNoLength ;
	    string inputno ;
	  
	    cin >> inputNoLength ;  // BINARY STRING LENGTH
	    cin >> inputno ;    //BINARY STRING
	    
	    string result = "" ;
	    
	    for(int i=0 ; i<inputNoLength ; i+=2){
	        string cum = inputno.substr(i, 2) ;

	        result = result +  m[cum] ;
	    }
    
      cout << result <<endl ;
	}
	    
	return 0 ;
}
