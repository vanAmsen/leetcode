/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfLevels(root *TreeNode) []float64 {
	if root == nil { 
			return []float64{} 
	} 

	var result []float64 
	queue := []*TreeNode{root} 

	for len(queue) > 0 { 
		levelSize := len(queue) 
		sum := 0 
		count := 0 

		for i := 0; i < levelSize; i++ { 
			node := queue[0] 
			queue = queue[1:] 
			sum += node.Val 
			count++ 

			if node.Left != nil { 
				queue = append(queue, node.Left) 
			} 
			if node.Right != nil { 
				queue = append(queue, node.Right) 
			} 
		} 

		result = append(result, float64(sum)/float64(count)) 
	} 

	return result 
																																		
}
