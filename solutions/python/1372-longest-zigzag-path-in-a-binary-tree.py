# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = 0 

        def dfs(node, direction, length): 
            nonlocal max_length 
            if not node: 
                return 
            # Update the maximum ZigZag length 
            max_length = max(max_length, length) 
            # If the current direction is 0 (left), move to the left child and change direction to 1 (right) 
            if direction == 0: 
                dfs(node.left, 1, length + 1) 
                dfs(node.right, 0, 1) 
            # If the current direction is 1 (right), move to the right child and change direction to 0 (left) 
            else: 
                dfs(node.right, 0, length + 1) 
                dfs(node.left, 1, 1) 

        dfs(root, 0, 0) 
        return max_length 
                                                                                                                                                                                                                               
