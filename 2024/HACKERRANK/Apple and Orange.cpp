// APPLE AND ORANGE , HACKERRANK , SOLN IN C++ 

void countApplesAndOranges(int s, int t, int a, int b, vector<int> apples, vector<int> oranges) {
  
    int count_apple = 0, count_orange = 0 ;

    for(int i=0; i<apples.size(); i++){
        int apple_coord =  a+ apples[i] ;
        
        if( (apple_coord >=s)&&(apple_coord <= t) ){
            count_apple ++ ;
        }
    }
    
    for (int i=0; i<oranges.size(); i++) {
        int orange_coord =  b + oranges[i]  ;
        
        if( (orange_coord >=s)&&(orange_coord <= t) ){
            count_orange ++ ;
        }
    }
    
    cout<<count_apple<<endl<<count_orange<<endl ;
}
