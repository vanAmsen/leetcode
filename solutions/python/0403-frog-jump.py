class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {} 
        for stone in stones: 
            dp[stone] = set() 
        dp[0].add(1) 

        for stone in stones: 
            for k in dp[stone]: 
                next_stone = stone + k 

                if next_stone in dp: 
                    if k - 1 > 0: 
                        dp[next_stone].add(k - 1) 
                    dp[next_stone].add(k) 
                    dp[next_stone].add(k + 1) 
        return len(dp[stones[-1]]) > 0 
                                                                                                                                                                                                                           
