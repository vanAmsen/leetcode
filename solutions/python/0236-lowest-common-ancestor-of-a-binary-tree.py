class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Step 1: Base Case 
        if root is None or root == p or root == q: 
            return root 

        # Step 2: Recursive Calls 
        left = self.lowestCommonAncestor(root.left, p, q) 
        right = self.lowestCommonAncestor(root.right, p, q) 

        # Step 3: Finding LCA 
        if left and right: 
            return root 
        return left if left else right 
                                             
