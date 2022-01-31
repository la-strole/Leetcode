import com.sun.source.tree.BreakTree;

public class Solution {


     public TreeNode sortedArrayToBST(int[] nums) {

          final class Helper {

              private TreeNode getRoot(int low, int hi) {

                  if (low > hi) return null;

                  int mid = (low + hi) / 2;
                  TreeNode node = new TreeNode(nums[mid]);

                  node.left = getRoot(low, mid - 1);
                  node.right = getRoot(mid + 1, hi);
                  return node;
              }
          }

          return new Helper().getRoot(0, nums.length - 1);

     }
}

