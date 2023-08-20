class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort() 
        left, right = 0, len(nums) - 1 
        count = 0 

        while left < right: 
            if nums[left] + nums[right] < target: 
                count += (right - left) 
                left += 1 
            else: 
                right -= 1 

        return count 
                                                                                                                          
