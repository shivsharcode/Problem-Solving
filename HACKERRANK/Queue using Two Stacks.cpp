#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    stack<int> s1, s2 ;
    
    int query_num ;     //no. of queries
    cin>>query_num ;
    
    int query, data ;  
    
    for (int i=0; i<query_num ; i++){
        cin>>query ;
        
        //1-Enqueue
        if(query==1){
            cin>>data ;
            s1.push(data) ;
        }
        
        //2-Dequeue
        if(query==2){
            //if s2 is not empty --> pop the top element -- first element of our queue
            if(!s2.empty()){
                s2.pop() ;
            }
            
            //if s2 is empty --> then rev the s1 stack to s2--> then pop the top elem
            else{
                while (!s1.empty()) {
                    s2.push(s1.top()) ;
                    s1.pop() ;
                }
                s2.pop() ;
            }
        }
        
        //3-Print the front element of queue
        if(query==3){
            //s2 is not empty --> print the top elem (front elem of queue)
            if(!s2.empty()){
                cout<<s2.top()<<endl ;
            }
            //s2 is empty --> rev the stack s1 to s2 --> print top elem(front of queue)
            else{
                while (!s1.empty()) {
                    s2.push(s1.top()) ;
                    s1.pop() ;
                }
                cout<<s2.top()<<endl ;
            }
        }
    }
    
    
    return 0;
}
