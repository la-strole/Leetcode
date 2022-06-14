/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    
    let local_maximum = nums[0];
    let global_maximum = nums[0];

    for (let i = 1; i < nums.length; i++) {
        local_maximum = Math.max(local_maximum + nums[i], nums[i]);
        global_maximum = Math.max(global_maximum, local_maximum);
    }

    return global_maximum;

};


var main = function() {
    let test_array = [-2,1,-3,4,-1,2,1,-5,4];
    console.log(`Result is ${maxSubArray(test_array)}`);
}

main();