//BREAKING THE RECORDS , SOLN IN C++

vector<int> breakingRecords(vector<int> scores) {
    
    int max=scores[0] ;
    int min = scores[0] ;
    int max_count=0, min_count = 0 ;
    
    for(int i=0; i<scores.size(); i++){
        
        if(scores[i]>max){
            max = scores[i] ;
            max_count ++ ;
           
        }
        else if (scores[i]<min) {
            min = scores[i] ;
            min_count ++ ;
        }
    }
    
    vector<int> MaxMin = {max_count, min_count} ;
    
    return MaxMin;
}
