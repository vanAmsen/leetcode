class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n 
        while left < right: 
            target = right - (right - left) // 2 
            if sum(min(battery, target) for battery in batteries) >= target * n: 
                left = target 
            else: 
                right = target - 1 
        return left 
                                                                                                        
