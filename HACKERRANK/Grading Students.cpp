// GRADING STUDENTS SOLN , HACKERRANK, SOLN IN C++

vector<int> gradingStudents(vector<int> grades) {
    
    for (int i=0; i<grades.size(); i++) {
        int mul = grades[i] / 5 ;
        mul ++ ;
        int next_multiple = mul * 5 ;
        
        if (grades[i] < 38) {
            //pass ;
        }
        
        else if( (next_multiple - grades[i]) < 3){
            grades[i] = next_multiple ;
        }
        
    }
    
    return grades ;
    
}
