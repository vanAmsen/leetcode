class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False 

        targetSum -= root.val 

        # Check if the current node is a leaf node 
        if not root.left and not root.right: 
            return targetSum == 0 

        # Recur for the left and right subtree 
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum) 
                                                                                                        
