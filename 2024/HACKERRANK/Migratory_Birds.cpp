//MIGRATORY BIRDS PROB , ------- USING VISITED ARRAY APPROACH



int migratoryBirds(vector<int> arr) {
    vector<int> sec(5) ;
    
    for (int i=0; i<arr.size(); i++){
        sec[arr[i]-1] ++ ;
    }
    
    int max_freq = sec[0] ;
    int ind  ;
    for(int i=0; i<sec.size(); i++){
        if(sec[i] > max_freq){
            max_freq = sec[i] ;  
            ind = i+1 ;   
        }
    }
    
    return ind ;
}
