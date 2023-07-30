class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: 
            return None 
        if root.val == val: 
            return root 
        elif root.val < val: 
            return self.searchBST(root.right, val) 
        else:  
            return self.searchBST(root.left, val)    
