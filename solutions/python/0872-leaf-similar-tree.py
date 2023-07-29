class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node): 
            if node: 
                if not node.left and not node.right: 
                    yield node.val 
                yield from dfs(node.left) 
                yield from dfs(node.right) 

        return list(dfs(root1)) == list(dfs(root2)) 
