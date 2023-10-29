class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        if n < 3: 
            return 0 

        # Initialize the dp array with size n and large values 
        dp = [float('inf')] * n 

        # Base cases 
        dp[0] = max(0, k - nums[0]) 
        dp[1] = max(0, k - nums[1]) 
        dp[2] = max(0, k - nums[2]) 

        # Fill in the dp array using the recursive formula 
        for i in range(3, n): 
            dp[i] = max(0, k - nums[i]) + min(dp[i-1], dp[i-2], dp[i-3]) 

        # Return the minimum of the last three values in dp 
        return min(dp[-1], dp[-2], dp[-3]) 
                                                                                                                                                          
