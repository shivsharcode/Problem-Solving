// BILL DIVISION SOLN , IN CPP

void bonAppetit(vector<int> bill, int k, int b) {
    
    
    int sum = std::accumulate(bill.begin(), bill.end(), 0) ;  //total bill //sum of vector
    
    int Anna_share = (sum - bill[k])/2 ;
    
    if(Anna_share == b){
        cout<<"Bon Appetit" ;
    }
    else{
        cout<< abs(b-Anna_share) ;
    }
    
}
