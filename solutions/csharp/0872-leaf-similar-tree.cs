public class Solution {
    public bool LeafSimilar(TreeNode root1, TreeNode root2) {
        IList<int> leaves1 = new List<int>();
        IList<int> leaves2 = new List<int>();
        Dfs(root1, leaves1);
        Dfs(root2, leaves2);
        return leaves1.SequenceEqual(leaves2);
    }

    public void Dfs(TreeNode node, IList<int> leafValues) {
        if (node != null) {
            if (node.left == null && node.right == null) {
                leafValues.Add(node.val);
            }
            Dfs(node.left, leafValues);
            Dfs(node.right, leafValues);
        }
    }
}
