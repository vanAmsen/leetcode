class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        # Initialize the current and next furthest reachable positions
        curr_furthest, next_furthest = nums[0], nums[0]
        
        jumps = 1  # At least one jump is needed to reach the end
        
        for i in range(1, len(nums)):
            if i > curr_furthest:
                jumps += 1
                curr_furthest = next_furthest
            
            next_furthest = max(next_furthest, i + nums[i])
        
        return jumps
