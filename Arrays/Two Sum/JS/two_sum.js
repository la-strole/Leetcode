var twoSum = function(nums, target) {
    /* create dictionary */
    let hash_table = {};

    for (let i = 0; i < nums.length; i++){
      let diff = target - nums[i];
      if (diff.toString() in hash_table){
      	return [i, hash_table[diff]];
      }
      else {
      	hash_table[nums[i]] = i;
      }
    }
};

var nums = [2,7,11,15];
var target = 9;
var result = twoSum(nums, target);
console.log(result);
