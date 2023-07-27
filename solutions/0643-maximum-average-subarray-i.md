# 🔢 Find the Maximum Average Subarray with Sliding Window Technique!

# Intuition
Given an array of integers and an integer `k`, the problem asks us to find the contiguous subarray of length `k` that has the maximum average value. My initial thought is to solve this problem using the sliding window technique. This technique is particularly effective when we need to track a certain property (like sum or average) of a contiguous subarray.

# Approach
We start by calculating the sum of the first `k` elements in the array. This sum will serve as our sliding window. We also initialize a variable `max_avg` to store the maximum average found so far, and set it equal to the average of the first `k` elements.

Then, we slide the window across the array one step at a time. With each slide, we add the next element in the array to the window and subtract the first element of the current window. After each slide, we calculate the average of the window's elements and compare it to `max_avg`. If the current average is greater, we update `max_avg`.

We continue this process until we've slid the window across the entire array. In the end, `max_avg` will hold the maximum average of any `k`-element subarray.

# Complexity
- Time complexity:
The time complexity of the solution is \(O(n)\), where `n` is the length of the array. This is because we're iterating over the array once.

- Space complexity:
The space complexity of the solution is \(O(1)\). We're using a fixed amount of space to store the window sum and the maximum average.

# Code
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = window_sum / k
        
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, window_sum / k)
            
        return max_avg
```
In the code, we implement the approach described above. We start by calculating the sum of the first `k` elements and storing this as the maximum average. Then, we slide the window one step at a time, updating the window sum and maximum average as we go. In the end, we return the maximum average.
