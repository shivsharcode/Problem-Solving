// BETWEEN TWO SETS,  soln in C++

int getTotalX(vector<int> a, vector<int> b) {
    
    sort(b.begin(), b.end()) ;
    
    vector<int> fact ;
    
    int count_desired_integer =0 ;
    
    
    for(int i=1; i<=b[0]; i++){
        int count = 0;
        for(int j=0; j<b.size(); j++){
            if(b[j] % i == 0){
                count++ ;
            }
        }
            if (count == b.size()) {
                fact.push_back(i) ;
                cout<<i<<endl ;
            }
        
    }
    
    for(int i=0; i<fact.size(); i++){
        int count = 0 ;
        
        for(int j=0; j<a.size(); j++){
            if(fact[i] % a[j] == 0){
                count ++ ;
            }
        }
        if(count == a.size()){
            count_desired_integer ++ ;
        }
    }
    
    return count_desired_integer ;
}
