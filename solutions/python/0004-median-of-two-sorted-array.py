class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1 

        m, n = len(nums1), len(nums2) 
        low, high = 0, m 

        while low <= high: 
            partitionX = (low + high) // 2 
            partitionY = (m + n + 1) // 2 - partitionX 

            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1] 
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1] 
            minX = float('inf') if partitionX == m else nums1[partitionX] 
            minY = float('inf') if partitionY == n else nums2[partitionY] 

            if maxX <= minY and maxY <= minX: 
                if (m + n) % 2 == 0: 
                    return (max(maxX, maxY) + min(minX, minY)) / 2 
                else: 
                    return max(maxX, maxY) 
            elif maxX > minY: 
                high = partitionX - 1 
            else: 
                low = partitionX + 1 
                                                                                                                                                                                                                                                                                                                        
