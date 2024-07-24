// APPROACH - CONDITIONAL STATEMENT, BUT THIS APPROACH IS SUITABLE ONLY FOR SMALL KEY-VALUES IF THE CODING CONTAINS MORE NUCLEOTIDES 


#include <bits/stdc++.h>
using namespace std;

int main() {
  
	int T ;  // input - Testcase
	cin >> T ;
	
	unordered_map <string, char> m ;
	
	while(T--){
	    int inputNoLength ;    //BINARY STRING LENGTH
	    string inputno ;      // BINARY STRING
	       
	    cin >> inputNoLength ;
	    cin >> inputno ;
	    
	    string result = "" ;
        
        for(int i=0; i<inputno.size(); i+=2 ){
            
            string cum = inputno.substr(i, 2) ;
            
            if(cum == "00"){
                result = result + 'A' ;
            }
            else if(cum == "01"){
                result = result + 'T' ;
            }
            else if(cum == "10"){
                result = result + 'C' ;
            }
            else if(cum == "11"){
                result = result + 'G' ;
            }
            // END OF FOR LOOP
        }
        
        cout << result << endl ;   
	}
	return 0 ;
}
