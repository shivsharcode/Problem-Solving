// APPROACH - using the .map array method

var map = function(arr, fn) {
    
    return arr.map( (val, idx)=>{

       return fn(val, idx) ;
    } ) ;
};
