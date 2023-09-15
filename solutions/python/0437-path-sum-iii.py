# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, cur_sum, prefix_sum_counter): 
            nonlocal count 
            if not node: 
                return 

            # Update the current path sum 
            cur_sum += node.val 

            # Check if there exists a subarray summing to targetSum 
            count += prefix_sum_counter.get(cur_sum - targetSum, 0) 

            # Update the prefix sum counter 
            prefix_sum_counter[cur_sum] = prefix_sum_counter.get(cur_sum, 0) + 1 

            # Recur for the left and right children 
            dfs(node.left, cur_sum, prefix_sum_counter) 
            dfs(node.right, cur_sum, prefix_sum_counter) 

            # Backtrack: remove the current node's value from the prefix sum counter 
            prefix_sum_counter[cur_sum] -= 1 
            if prefix_sum_counter[cur_sum] == 0: 
                del prefix_sum_counter[cur_sum] 

        count = 0 
         # Initialize with a zero sum having a frequency of 1 
        prefix_sum_counter = {0: 1}  
        dfs(root, 0, prefix_sum_counter) 
        return count 
                                                                                                                                                                                                                                                                                                                           
