class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0 
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        previous = [0] * cols
        current = [0] * cols
        previous[0] = 1 
        
        for r in range(rows):
            current[0] = 0 if obstacleGrid[r][0] == 1 else previous[0]            
            for c in range(1, cols):
                current[c] = 0 if obstacleGrid[r][c] == 1 else current[c-1] + previous[c]
            
            previous[:] = current
        
        return previous[cols-1]
