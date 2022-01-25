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
 var isSymmetric = function(root) {

   
    
    let helper = function(leftChild, rightChild) {

        if (leftChild == null || rightChild == null) {
            return leftChild == rightChild;
        }

        if (leftChild.val != rightChild.val) {
            return false;
        }

        return helper(leftChild.left, rightChild.right) && helper(leftChild.right, rightChild.left);
    }

    return root == null || helper(root.left, root.right);
};