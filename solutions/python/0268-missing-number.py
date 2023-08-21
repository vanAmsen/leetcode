class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_result = len(nums) 

        for i, num in enumerate(nums): 
            xor_result ^= i ^ num 

        return xor_result 
                                                            
