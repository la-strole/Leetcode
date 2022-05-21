/**
 * @param {number[]} nums
 */
 var Solution = function(nums) {
    this.original = nums.slice();
    this.nums = nums;
};

/**
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    this.nums = [...this.original];
    return this.nums;
};

/**
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
    for (let index = 0; index < this.nums.length; index++) {
        let temp = this.nums[index] ;
        this.nums[index] = Math.floor(Math.random() * (this.nums.length - index) + index);
    }
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */