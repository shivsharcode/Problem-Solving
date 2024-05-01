// MIGRATORY BIRDS PROB ----- USING UNORDERED HASHMAP

int migratoryBirds(vector<int> arr) {
    
    unordered_map<int, int> freq ;      //unordered hashmap  -- first ind : key ,, second int : value ;
    
    //count the freq of each type
    for (int bird : arr){
        freq[bird] ++ ;
    }
    
    int max_freq = 0 ;
    int type = 0 ;
    
    for(auto & i: freq){
        if(i.second > max_freq || (i.second == max_freq && i.first < type)){          //first = key, second = value 
            max_freq = i.second ;
            type = i.first ;
        }
    }
    
    return type ;
}
