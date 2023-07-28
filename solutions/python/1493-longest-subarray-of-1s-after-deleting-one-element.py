class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, count_zeros, max_length = 0, 0, 0 
        for right in range(len(nums)): 
            if nums[right] == 0: 
                count_zeros += 1 
            while count_zeros > 1: 
                if nums[left] == 0: 
                    count_zeros -= 1 
                left += 1 
            max_length = max(max_length, right-left) 
        return max_length 
                                                                                                                                              
