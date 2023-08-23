class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create frequency counters for both arrays
        c1, c2 = Counter(nums1), Counter(nums2)
        
        # Take the intersection of both frequency counters
        intersection = c1 & c2
        
        # Convert the intersection frequency counter back to list
        result = []
        for num, freq in intersection.items():
            result.extend([num] * freq)
        
        return result
