import javax.swing.tree.TreeNode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {

        return root == null || helper(root.left, root.right);
    }

    private static boolean helper(TreeNode leftChild, TreeNode rightChild) {

        if (leftChild == null || rightChild == null ) {
            return leftChild == rightChild;
        }

        if (leftChild.val != rightChild.val) {
            return false;
        }

        return helper(leftChild.left, rightChild.right) && helper(leftChild.right, rightChild.left);
    }
}