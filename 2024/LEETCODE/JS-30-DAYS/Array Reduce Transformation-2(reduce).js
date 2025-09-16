// APPROACH - .reduce(accumulator, val) array method

// USING .reduce()
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {

    nums.unshift(init) ;

    return nums.reduce( (accumulator, val) =>{
        return fn(accumulator, val) ;
        }   
    ) ;
};
