class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, target): 
            # Base case 
            if len(path) == k and target == 0: 
                res.append(list(path)) 
                return 
            for i in range(start, 10):  # numbers 1 through 9 
                if i > target:  # not possible to get the combination 
                    break 
                # Recursive call 
                backtrack(i + 1, path + [i], target - i) 

        res = [] 
        backtrack(1, [], n) 
        return res 
                                                                                                                                                                                   
