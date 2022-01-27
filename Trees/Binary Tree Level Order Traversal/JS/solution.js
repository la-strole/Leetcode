
//  Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/*
 @param {TreeNode} root
 @return {number[][]}
 */
 var levelOrder = function(root) {

    if (root == null) return [];

    const queue = [root,];
    const answer = [];
    var level = [];
    
    while (queue.length != 0) {

        level = [];

        let size = queue.length;

        for (let i = 0; i < size; i++) {

            let current_node = queue.pop();
            
            level.push(current_node.val)

            if (current_node.left != null) {
                queue.unshift(current_node.left);
            }
            if (current_node.right != null) {
                queue.unshift(current_node.right);
            }

        }

        answer.push(level);

    }

    return answer;
};