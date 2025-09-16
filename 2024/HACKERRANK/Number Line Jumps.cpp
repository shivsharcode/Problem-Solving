// NUMBER LINE JUMPS , HACKERRANK, SOLN IN C++

string kangaroo(int x1, int v1, int x2, int v2) {
    
    int pos1 = x1, pos2 = x2 ;
    while (pos1<= pos2) {
        pos1 += v1 ;
        pos2 += v2 ;
        
        if(pos1 == pos2){
            return "YES" ;
        }
    }
    
    return "NO" ;
}
