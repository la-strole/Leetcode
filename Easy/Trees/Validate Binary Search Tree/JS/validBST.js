/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var isValidBST = function(root, low=-Infinity, hi=Infinity) {
    if (root) {
        if (root.val <= low || root.val >= hi) {
            return false;
        }
        return isValidBST(root.left, lo, root.val) && isValidBST(root.right, root.val, hi);
    }
    return true;
};