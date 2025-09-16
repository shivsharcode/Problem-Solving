// BIRTHDAY CAKE CANDLES SOLN IN C++/C : 

int birthdayCakeCandles(vector<int> candles) {
    
    int max = 0;
    int count = 0 ;
    
    for (int i=0; i<candles.size(); i++) {
        if(candles[i]>max){
            max = candles[i] ;
            count=1 ;
        }
        
        else if(candles[i]==max){
            count ++ ;
        }
    }
    return count ;
}
