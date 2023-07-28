# 💡 Intuition
Given a binary array, we are to delete one element and then find the longest non-empty subarray that only contains 1's. My initial idea to solve this problem is to use the sliding window technique.

https://youtu.be/zqZ1vQg1WDM

# 🧠 Approach
My approach is to iterate over the array and keep a count of the zeros in our current window. If the count of zeros goes above 1, we move the left boundary of the window forward until we have at most one zero in our window. At each step, we also keep track of the maximum length of the window, which will ultimately give us the longest subarray of 1's after deleting one element.

# ⏲️ Complexity
- Time complexity: The time complexity of the algorithm is O(n) where n is the length of the input array. This is because we traverse the array once.

- Space complexity: The space complexity of the algorithm is O(1) because we are not using any additional data structures whose size depends on the input.

# 📝 Code
``` Python []
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, count_zeros, max_length = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1
            while count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
            max_length = max(max_length, right-left)
        return max_length
```
``` C# []
public class Solution {
    public int LongestSubarray(int[] nums) {
        int left = 0, count_zeros = 0, max_length = 0;
        for (int right = 0; right < nums.Length; ++right) {
            if (nums[right] == 0) {
                ++count_zeros;
            }
            while (count_zeros > 1) {
                if (nums[left] == 0) {
                    --count_zeros;
                }
                ++left;
            }
            max_length = Math.Max(max_length, right - left);
        }
        return max_length;
    }
}
```
``` JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let left = 0, count_zeros = 0, max_length = 0;
    for (let right = 0; right < nums.length; ++right) {
        if (nums[right] == 0) {
            ++count_zeros;
        }
        while (count_zeros > 1) {
            if (nums[left] == 0) {
                --count_zeros;
            }
            ++left;
        }
        max_length = Math.max(max_length, right - left);
    }
    return max_length;
};
```
``` Java []
public class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0, count_zeros = 0, max_length = 0;
        for (int right = 0; right < nums.length; ++right) {
            if (nums[right] == 0) {
                ++count_zeros;
            }
            while (count_zeros > 1) {
                if (nums[left] == 0) {
                    --count_zeros;
                }
                ++left;
            }
            max_length = Math.max(max_length, right - left);
        }
        return max_length;
    }
}
```
``` C++ []
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0, count_zeros = 0, max_length = 0;
        for (int right = 0; right < nums.size(); ++right) {
            if (nums[right] == 0) {
                ++count_zeros;
            }
            while (count_zeros > 1) {
                if (nums[left] == 0) {
                    --count_zeros;
                }
                ++left;
            }
            max_length = max(max_length, right - left);
        }
        return max_length;
    }
};
```
