public class Solution {
    public TreeNode SearchBST(TreeNode root, int val) {
        if (root == null) {
            return null;
        }
        if (root.val == val) {
            return root;
        }
        if (root.val < val) {
            return SearchBST(root.right, val);
        }
        return SearchBST(root.left, val);
    }
}
