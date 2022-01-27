
import java.util.*;

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> answer = new ArrayList<>();

        if (root == null) return answer;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            List<Integer> level_nodes = new ArrayList<>();
            int sizeOfQueue = queue.size();

            for (int i = 0; i < sizeOfQueue; i++) {
                TreeNode current_node = queue.remove();
                level_nodes.add(current_node.val);
                if (current_node.left != null) {
                    queue.add(current_node.left);
                }
                if (current_node.right != null) {
                    queue.add(current_node.right);
                }
            }

            answer.add(level_nodes);
        }

        return answer;
    }
}
