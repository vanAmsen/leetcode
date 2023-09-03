class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)] 

        for i in range(1, m): 
            for j in range(1, n): 
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 

        return dp[-1][-1] 
                                                                                       
