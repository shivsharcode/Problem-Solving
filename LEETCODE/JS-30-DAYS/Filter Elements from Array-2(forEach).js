// using forEach

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArr = [] ;
    arr.forEach( (val, idx)=>{
        if(fn(val, idx)){
            filteredArr.push( val ) ;
        }
    } ) ;

    return filteredArr ;
    
};
