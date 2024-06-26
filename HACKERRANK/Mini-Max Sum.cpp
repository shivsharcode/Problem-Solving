// MINI-MAX SUM soln in C++ 

#include<algorithm>
#include<iostream>
#include<vector>

using namespace std ;

void miniMaxSum(vector<int> arr) {
    
    sort(arr.begin(), arr.end()) ;
    long min =0 , max = 0 ;
    
    for (int i=0; i<arr.size(); i++) {
        if (i<4) {
            min = min + arr[i] ;
        }   
        if(i>0){
            max = max + arr[i] ;
        }
    }
    
    cout<<min<<" "<<max  ;
}
