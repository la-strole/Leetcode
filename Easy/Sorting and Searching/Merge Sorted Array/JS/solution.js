/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
 var merge = function(nums1, m, nums2, n) {
    
    // Create pointers
    let leftPointer = m - 1;
    let rightPointer = n - 1;
    let currentPointer = m + n - 1;

    // Iterate trough nums1 and nums2. max elements
    while (leftPointer >= 0 && rightPointer >= 0) {

        if (nums1[leftPointer] >= nums2[rightPointer]) {
            nums1[currentPointer] = nums1[leftPointer];
            leftPointer--;
        }
        else {
            nums1[currentPointer] = nums2[rightPointer];
            rightPointer--;
        }
        currentPointer--;
    }

    // extend nums1 with nums2 min values
    if (rightPointer >= 0){
        for (let i = 0; i <= rightPointer; i++){
            nums1[i] = nums2[i];
        }
    }
};

nums1 = [4,5,6,0,0,0];
m = 3;

nums2 = [1,2,3];
n = 3;

merge(nums1, m, nums2, n);

console.log(`Result is ${nums1}`);