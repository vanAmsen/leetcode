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
