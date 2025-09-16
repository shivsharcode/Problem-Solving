// APPROACH - USING .forEach() method 

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let newArr = [] ;

    arr.forEach( (val, idx)=>{
        newArr.push( fn(val, idx) ) ;
    } ) ;

    return newArr ;
};
