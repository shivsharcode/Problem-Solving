// TIME CONVERSION PROBLEM , HACKERRANK , SOLN IN C++ 

string timeConversion(string s) {

    if (s[8] == 'P' || s[8]== 'p') {
        s.erase(8,2) ;
        
        if(s[0]=='1' && s[1]=='2'){
            //pass
        }
        else{
            s[0] = (int)s[0] + 1 ;
            s[1] = (int)s[1] + 2 ;
        }
    }
    
    else if (s[8] == 'A' || s[8]== 'a'){
        s.erase(8,2) ;
        if(s[0]=='1' && s[1] == '2'){
            s[0] = '0' ;
            s[1] = '0' ;
        }
    }
    return s;
}
