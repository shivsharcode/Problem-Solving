
#include <iostream>
#include <vector>


using namespace std ;

void extraLongFactorials(int n) {
    
    vector<int> arr ;
    arr.push_back(1) ;      //start with adding 1  to the vector arr
    
    //calculation
    for(int i=2; i<=n ; i++){
        int carry = 0 ;
        int size = arr.size() ;
        
        for(int j=0; j<size ;j++){
            
            int value = arr[j]*i + carry ;
            arr[j] = value%10 ;
            carry = value/10 ;
        }
        while (carry) {
            arr.push_back(carry%10) ;
            carry /= 10 ;
        }
    }
    
    //print the vector containing fact
    for(int i=arr.size()-1 ;i>=0; i--){
        cout<<arr[i] ;
    }

}


int main(){

    int n ;
    cout<<"Enter the number : " ;
    cin>>n ;

    extraLongFactorials(n) ;

    return 0 ;
}