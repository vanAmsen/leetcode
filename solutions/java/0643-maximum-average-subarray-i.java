public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double window_sum = 0;
        for (int i = 0; i < k; i++) {
            window_sum += nums[i];
        }
        double max_avg = window_sum;

        for (int i = k; i < nums.length; i++) {
            window_sum += nums[i] - nums[i - k];
            max_avg = Math.max(max_avg, window_sum);
        }
        return max_avg / k;
    }
}
