class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def in_order_traversal(node): 
            nonlocal current_val, current_count, max_count, modes 
            if not node: 
                return 

            # Traverse left subtree 
            in_order_traversal(node.left) 

            # Process current node 
            current_count = current_count + 1 if node.val == current_val else 1 
            current_val = node.val 

            if current_count > max_count: 
                max_count = current_count 
                modes = [current_val] 
            elif current_count == max_count: 
                modes.append(current_val) 

            # Traverse right subtree 
            in_order_traversal(node.right) 

        current_val = None 
        current_count = 0 
        max_count = 0 
        modes = [] 
        in_order_traversal(root) 
        return modes 
                                                                                                                                                                                                                                                                                                                          
