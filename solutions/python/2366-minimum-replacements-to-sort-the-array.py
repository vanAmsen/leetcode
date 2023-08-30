class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0 
        prev_bound = nums[-1] 

        for num in reversed(nums[:-1]): 
            no_of_times = (num + prev_bound - 1) // prev_bound 
            operations += no_of_times - 1 
            prev_bound = num // no_of_times 

        return operations 
                                                                                     
