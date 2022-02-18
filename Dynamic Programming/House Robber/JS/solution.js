/**
 * @param {number[]} nums
 * @return {number}
 */
 var rob = function(nums) {
    
    if (nums.length == 1) { return nums[0]; }
    if (nums.length == 2) { return Math.max(nums[0], nums[1]); }

    let helperArray = nums.slice();

    helperArray[2] = helperArray[0] + helperArray[2];

    for (let i = 3; i < nums.length; i++) {
        helperArray[i] = helperArray[i] + Math.max(helperArray[i-3], helperArray[i-2]);
    }
    
    
    return Math.max.apply(Math, helperArray);

};

let test_Array = [2,7,9,3,1];
console.log(`Result is ${rob(test_Array)}`);