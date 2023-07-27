class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf') 
        window_sum = 0 
        for i in range(len(nums)): 
            window_sum += nums[i] 
            if i >= k - 1: 
                max_avg = max(max_avg, window_sum / k) 
                window_sum -= nums[i - k + 1]  
        return max_avg 
                                                                                                
