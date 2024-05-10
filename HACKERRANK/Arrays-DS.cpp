// ARRAYS-DS PROB , HACKERRANK, DATA STRUCTURE, 
// O(n/2)

// APPROACH - SWAPPING FROM BEGIN AND ENDING

vector<int> reverseArray(vector<int> a) {
    
    int n = a.size() ;
    int temp ;
    for(int i=0; i < n/2 ; i++){
        //swap
        temp = a[i] ;
        a[i] = a[n-1-i] ;
        a[n-1-i] = temp ;
        
    }
    return a ;;
}
