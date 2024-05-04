//PAIRS APPROACH- BRUTE FORCE , SOLN IN CPP

// O(N^2) - NOT PREFERRED

int pairs(int k, vector<int> arr) {
    
    sort(arr.begin(), arr.end()) ;
    int pairs_count = 0 ;
    
    for (int i=arr.size()-1; i>=0; i--) {
        
        for (int j=i-1; j>=0; j--) {
            if (arr[i]-arr[j] == k) {
                pairs_count ++ ;
            }
            if(arr[i]-arr[j]>k){
                break;
            }
        }
    }
    
    return pairs_count;
    
    
    
}
