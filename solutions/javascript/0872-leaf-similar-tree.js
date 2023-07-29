/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    const dfs = (node, leaves) => {
    if (node === null) return;
    if (!node.left && !node.right) {
        leaves.push(node.val);
    }
    dfs(node.left, leaves);
    dfs(node.right, leaves);
    }

    const leaves1 = [], leaves2 = [];
    dfs(root1, leaves1);
    dfs(root2, leaves2);
    return JSON.stringify(leaves1) === JSON.stringify(leaves2);
};
