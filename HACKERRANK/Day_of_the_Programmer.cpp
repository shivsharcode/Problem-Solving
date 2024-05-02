// DAY OF THE PROGRAMMER SOLN , IN C++

string dayOfProgrammer(int year) {
    
    string s_year = to_string(year) ;
    
    string leap_date = "12.09." + s_year ;
    string not_leap_date = "13.09." + s_year ;
    
    if(year>1918) {
        //gregorian
        if(year%400 == 0 || ( (year%4==0)&&(year%100 != 0) ) ){
            return leap_date ;
        }
        else {
        return not_leap_date;
        }
    }
    else if (year == 1918) {
        //transition year
        return "26.09.1918" ;
        
    }
    else{
        if(( year%4==0) ){
            return leap_date ;
        }
        else {
        return not_leap_date;
        }
    }
}
