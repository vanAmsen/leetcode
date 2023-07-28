# Intuition
When first approaching this problem, the task seems to be a matter of finding balance within an array. The "pivot" point is where the sums on both sides are equal. A clear intuition here is to maintain two sums: a total sum of the entire array and a running sum that begins from the start of the array and increments as we traverse. Comparing these two sums as we move along the array could potentially lead us to the pivot index.

https://youtu.be/u_nTn_Rl9g0

# Approach
We leverage the prefix sum technique to solve this problem. First, we calculate the total sum of the array. Then we iterate over the array, maintaining a running sum (which is initially zero) that represents the sum of all the numbers to the left of the current index. 

For each index, we check if the running sum is equal to the total sum minus the running sum and the current number (which would represent the sum of all numbers to the right of the current index). If they are equal, we have found the pivot index and return it. 

If we traverse the entire array without finding a pivot index, we return -1, as the problem statement specifies.

# Complexity
- Time complexity: 
The time complexity is \(O(n)\), where \(n\) is the length of the array. This is because we make a single pass through the array.

- Space complexity:
The space complexity is \(O(1)\), as we use a fixed amount of space to store the total sum and the running sum.

This code perfectly demonstrates the approach we described. It uses the built-in sum() function to calculate the total sum, and then iterates through the array, checking at each index if the running sum equals the sum of numbers to the right. The pivot index is then returned if found, or -1 if not.

# Code
```Python []
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        
        return -1
```
``` C++ []
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        int leftSum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
};
```
``` Java []
public class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        int leftSum = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}
```
``` JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let totalSum = nums.reduce((a, b) => a + b, 0);
    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        if (leftSum === totalSum - leftSum - nums[i]) {
            return i;
        }
        leftSum += nums[i];
    }
    return -1;
};
```
``` C# []
public class Solution {
    public int PivotIndex(int[] nums) {
        int totalSum = nums.Sum();
        int leftSum = 0;
        for (int i = 0; i < nums.Length; ++i) {
            if (leftSum == totalSum - leftSum - nums[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}
```
