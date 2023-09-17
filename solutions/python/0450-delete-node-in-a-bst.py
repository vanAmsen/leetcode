class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Step 1: Locate the Node
        if not root:
            return None
        
        if root.val == key:
            # Step 2: Delete the Node
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            min_larger_node = root.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            
            root.val = min_larger_node.val
            root.right = self.deleteNode(root.right, min_larger_node.val)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        
        # Step 3: Return the Root
        return root
