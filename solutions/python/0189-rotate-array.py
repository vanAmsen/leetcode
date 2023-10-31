class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums) 
        k %= n 
        self.reverse(nums, 0, n-1) 
        self.reverse(nums, 0, k-1) 
        self.reverse(nums, k, n-1) 

    def reverse(self, nums: List[int], start: int, end: int) -> None: 
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start] 
            start, end = start + 1, end - 1 
                                                                                   
