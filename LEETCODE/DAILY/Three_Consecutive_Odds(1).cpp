class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {

        if(arr.size() <3 ){return false ;}  //if the array of size less than 3 

        for (int i = 0; i <= arr.size() - 3; i++) { // Ensure we don't go out of bounds
            
            if( (arr[i]%2 != 0) && (arr[i+1]%2 != 0) && (arr[i+2]%2 != 0) ){
                return true ;
            }
        }

        return false;
    }
};
