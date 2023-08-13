class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums) 

        # If the array has only one element, then not possible to partition into valid subarrays 
        if n == 1: 
            return False 

        # Initialization for the first three values 
        dp = [True, False, nums[0] == nums[1] if n > 1 else False] 

        for i in range(2, n): 
            current_dp = False 

            # Check for 2 equal elements 
            if nums[i] == nums[i-1] and dp[1]: 
                current_dp = True 

            # Check for 3 equal elements 
            elif i-2 >= 0 and nums[i] == nums[i-1] == nums[i-2] and dp[0]: 
                current_dp = True 

            # Check for 3 consecutive increasing elements 
            elif i-2 >= 0 and nums[i] - nums[i-1] == 1 and nums[i-1] - nums[i-2] == 1 and dp[0]: 
                current_dp = True 

            # Move the window forward 
            dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp 

        return dp[2] 
                                                                                                                                                                                                                                                                                                            
