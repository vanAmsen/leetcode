public class Solution {
    public int CountCompleteSubarrays(int[] nums) {
        int n = nums.Length;
        HashSet<int> set = new HashSet<int>(nums);
        int distinct_elements = set.Count;
        int count = 0;
        int left = 0;
        int right = 0;
        Dictionary<int, int> counter = new Dictionary<int, int>();

        while (right < n) {
            if (!counter.ContainsKey(nums[right])) {
                counter[nums[right]] = 0;
            }
            counter[nums[right]]++;
            while (counter.Count == distinct_elements) {
                counter[nums[left]]--;
                if (counter[nums[left]] == 0) {
                    counter.Remove(nums[left]);
                }
                left++;
                count += n - right;
            }
            right++;
        }
        return count;        
    }
}
