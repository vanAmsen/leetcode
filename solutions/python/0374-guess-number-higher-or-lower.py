class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n 
        while left <= right: 
            mid = left + (right - left) // 2 
            res = guess(mid) 
            if res == 0: 
                return mid 
            elif res < 0: 
                right = mid - 1 
            else: 
                left = mid + 1 
        return -1 
