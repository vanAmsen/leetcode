class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2) 

        # Initialize the current and previous rows 
        current = [float('-inf')] * (n + 1) 
        previous = [float('-inf')] * (n + 1) 

        for i in range(1, m + 1): 
            for j in range(1, n + 1): 
                # Current pair of elements dot product 
                curr_product = nums1[i-1] * nums2[j-1] 

                # Update the dp value considering various cases 
                current[j] = max(curr_product, previous[j], current[j-1], curr_product + max(0, previous[j-1])) 

            # Swap the current and previous rows 
            current, previous = previous, current 

        return previous[n] 
                                                                                                                                                                                                           
