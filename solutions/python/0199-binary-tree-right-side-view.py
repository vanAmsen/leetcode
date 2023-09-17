class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return [] 

        # Step 1: Initialize a Queue 
        queue = deque([root]) 
        right_view = [] 

        # Step 2: Traverse Each Level 
        while queue: 
            level_length = len(queue) 

            for i in range(level_length): 
                current_node = queue.popleft() 

                # Step 3: Grab the Rightmost Node 
                if i == level_length - 1: 
                    right_view.append(current_node.val) 

                if current_node.left: 
                    queue.append(current_node.left) 
                if current_node.right: 
                    queue.append(current_node.right) 

        return right_view 
