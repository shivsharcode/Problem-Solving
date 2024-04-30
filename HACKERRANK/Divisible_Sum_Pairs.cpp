// DIVISIBLE SUM PAIRS SOLN, IN C++ 

int divisibleSumPairs(int n, int k, vector<int> ar) {
    
    sort(ar.begin(), ar.end()) ;
    
    int pairs = 0 ;
    
    for (int i=0; i<ar.size(); i++) {
        
        for (int j=i+1; j<ar.size(); j++) {
            if( (ar[i] + ar[j])%k == 0 ){
                pairs ++ ;
            }
        }
    }
    
    return pairs;
    
}
