
//  Definition for a binary tree node.
 function TreeNode(val, left, right) {
     this.val = (val===undefined ? 0 : val)
     this.left = (left===undefined ? null : left)
     this.right = (right===undefined ? null : right)
 }
 
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
 var sortedArrayToBST = function(nums) {
    
    var hepler = function(low, hi) {

        if (low > hi) return null;

        let mid = Math.floor((low + hi) / 2);

        let node = new TreeNode(val=nums[mid]);

        node.left = hepler(low, mid - 1);
        node.right = hepler(mid + 1, hi);

        return node;    
    }

    return hepler(0, nums.length - 1);

};