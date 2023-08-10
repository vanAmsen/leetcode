class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1 

        while low <= high: 
            mid = (low + high) // 2 
            if nums[mid] == target: 
                return True 

            # If we cannot determine the sorted half due to duplicates 
            if nums[low] == nums[mid]: 
                low += 1 
                continue 

            # If left half is sorted 
            if nums[low] <= nums[mid]: 
                if nums[low] <= target <= nums[mid]: 
                    high = mid - 1 
                else: 
                    low = mid + 1 
            # If right half is sorted 
            else: 
                if nums[mid] <= target <= nums[high]: 
                    low = mid + 1 
                else: 
                    high = mid - 1 

        return False 
                                                                                                                                                                                                                                                                                                                                                                              
