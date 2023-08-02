class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
