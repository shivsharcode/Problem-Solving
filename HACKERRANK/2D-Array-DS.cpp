//HACKERRANK - 2D ARRAY DS PROB 
// APPROACH - BRUTE FORCE - NESTED LOOP
// O(N^2)

int hourglassSum(vector<vector<int>> arr) {
    
    int max = -9999 ;
    
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            int sum1 = arr[i][j] + arr[i][j+1] + arr[i][j+2] ;
            int sum2 = arr[i+1][j+1] ;
            int sum3 = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] ;
            
            int sum = sum1 + sum2 + sum3 ;
            
            if(sum > max){
                max = sum ;
            }
        }
    }
    
    return max ;
}
