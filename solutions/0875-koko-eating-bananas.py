class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate hours needed to eat all bananas with a given speed 
        def hours_needed(speed): 
            return sum((pile - 1) // speed + 1 for pile in piles) 

        # Initialize low and high for binary search 
        low, high = 1, max(piles) 

        # Binary search 
        while low <= high: 
            mid = (low + high) // 2 

            # Check how many hours it would take for Koko to eat all the bananas at this speed 
            if hours_needed(mid) <= h: 
                high = mid - 1 
            else: 
                low = mid + 1 

        return low 
                                                                                                                                                                                                  
