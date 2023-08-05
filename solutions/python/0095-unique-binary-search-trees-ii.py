class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate_trees(1, n) if n else [] 

    def generate_trees(self, start, end): 
        if start > end: 
            return [None,] 

        all_trees = [] 
        for i in range(start, end + 1):   
            left_trees = self.generate_trees(start, i - 1)  
            right_trees = self.generate_trees(i + 1, end)   

            for l in left_trees: 
                for r in right_trees: 
                    root = TreeNode(i) 
                    root.left = l 
                    root.right = r 
                    all_trees.append(root) 

        return all_trees 
