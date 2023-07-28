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
