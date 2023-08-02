class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        result = [1] * n 
        # Compute the prefix product for each element 
        prefix_product = 1 
        for i in range(n): 
            result[i] *= prefix_product 
            prefix_product *= nums[i] 
        # Compute the suffix product for each element and multiply it with the prefix product 
        suffix_product = 1 
        for i in range(n - 1, -1, -1): 
            result[i] *= suffix_product 
            suffix_product *= nums[i] 
        return result 
                                                                                                                           
