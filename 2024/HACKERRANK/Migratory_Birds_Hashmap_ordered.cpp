// MIGRATORY BIRDS PROB ----- USING ORDERED HASHMAP

int migratoryBirds(vector<int> arr) {
    
    map<int, int> freq ;      //ordered hashmap - the one which is sorted
    
    //count the freq of each type
    for (int bird : arr){
        freq[bird] ++ ;
    }
    
    int max_freq = 0 ;
    int type = 0 ;
    
    for(auto & i: freq){
        if(i.second > max_freq ){
            max_freq = i.second ;
            type = i.first ;
        }
    }
    
    return type ;
}
