/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func goodNodes(root *TreeNode) int {
    // Initialize with the lowest possible value (-10^5) 
   return dfs(root, -1e5) 
         
}

// Helper function for DFS traversal. 
func dfs(node *TreeNode, maxVal int) int { 
   if node == nil { 
       return 0 
   } 

   // Count the current node as a good node if its value is greater than or equal to the maximum value on the path 
   count := 0 
   if node.Val >= maxVal { 
  count = 1 
       maxVal = node.Val 
   } 

   // Continue DFS on the left and right subtrees 
   count += dfs(node.Left, maxVal) 
   count += dfs(node.Right, maxVal) 

   return count 
} 
                                           
