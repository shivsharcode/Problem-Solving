#include<bits/stdc++.h>
using namespace std ;

int main()
{
    int T ; //TESTCASES
    cin>>T ;
    cin.ignore() ;
    
    while(T--){
        
        int poolPrize ;
        cin >> poolPrize ;
        
        string matchResult ;
        cin >> matchResult ;
        
        int c=0, n=0, d=0 ;
        
        for(char &ch : matchResult){
            if(ch == 'C'){
                c += 1 ;
            } 
            else if(ch == 'D'){
                d += 1 ;
            }
            else if(ch == 'N'){
                n += 1 ;
            }
        }
        
        int carlsonPoints = (c*2) + (d*1) ;
        int chefPoints = (n*2) + (d*1) ;
        
        if(carlsonPoints > chefPoints){
            cout<< 60 * poolPrize << endl;
        }
        else if(carlsonPoints == chefPoints){
            cout<< 55 * poolPrize << endl ;
        }
        else if(carlsonPoints < chefPoints){
            cout<< 40 * poolPrize << endl  ;
        }
  
    }
    
    return 0 ;
}
