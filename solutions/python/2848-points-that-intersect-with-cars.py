class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Step 1: Sort the intervals based on their starting points 
        nums.sort(key=lambda x: x[0]) 

        # Step 2: Initialize count, start and end 
        count = 0 
        start = float('-inf') 
        end = float('-inf') 

        # Step 3: Iterate through the sorted intervals 
        for s, e in nums: 
            if s > end: 
                # Add the length of the current [start, end] interval to count 
                count += end - start + 1 if end != float('-inf') else 0 

                # Update start and end 
                start, end = s, e 
            else: 
                # Update end 
                end = max(end, e) 

        # Step 4: Add the length of the last [start, end] interval to count 
        count += end - start + 1 

        return count 
                                                                                                                                                                                                                                                                 
