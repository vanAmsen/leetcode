public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
        double window_sum = 0;
        for (int i = 0; i < k; i++) {
            window_sum += nums[i];
        }
        double max_avg = window_sum / k;

        for (int i = k; i < nums.Length; i++) {
            window_sum += nums[i] - nums[i - k];
            max_avg = Math.Max(max_avg, window_sum / k);
        }
        return max_avg;
    }
}
