class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 

        # Calculate the height of the left subtree 
        left_height = 0 
        node = root 
        while node.left: 
            left_height += 1 
            node = node.left 

        # Calculate the height of the right subtree 
        right_height = 0 
        node = root 
        while node.right: 
            right_height += 1 
            node = node.right 

        # If both heights are the same, the tree is perfect 
        if left_height == right_height: 
            return 2 ** (left_height + 1) - 1 

        # Otherwise, the tree is complete but not perfect 
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) 
                                                                                    
