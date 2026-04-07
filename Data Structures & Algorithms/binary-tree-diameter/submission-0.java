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
    private int ans=0;
    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return ans;
    }
    private int depth(TreeNode node){
        if (node==null){
            return 0;
        }
        int leftDepth=depth(node.left);
        int rightDepth=depth(node.right);

        ans=Math.max(ans,leftDepth+rightDepth);
        return Math.max(leftDepth,rightDepth)+1;
    }
}
