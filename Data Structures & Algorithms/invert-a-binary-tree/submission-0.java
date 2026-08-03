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
    public TreeNode invertTree(TreeNode root) {
        preOrder(root);
        return root; 
    }

    private void preOrder(TreeNode node) {
        TreeNode cur = node;
        if (node != null) {
            System.out.print(node.val);
            TreeNode tmp = node.left;
            node.left = node.right;
            node.right = tmp; 
            preOrder(node.left);
            preOrder(node.right);
        }
    }
}
