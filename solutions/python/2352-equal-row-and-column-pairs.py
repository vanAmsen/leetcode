class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0 
        n = len(grid)
        row_counter = collections.Counter(tuple(row) for row in grid) 
        for c in range(n): 
            col = [grid[i][c] for i in range(n)] 
            count += row_counter[tuple(col)] 
        return count 
                                                                                                                
