class Solution {
    public int countCompleteSubarrays(int[] nums) {
        int n = nums.length;
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        int distinct_elements = set.size();
        int count = 0;
        int left = 0;
        int right = 0;
        Map<Integer, Integer> counter = new HashMap<>();

        while (right < n) {
            counter.put(nums[right], counter.getOrDefault(nums[right], 0) + 1);
            while (counter.size() == distinct_elements) {
                counter.put(nums[left], counter.get(nums[left]) - 1);
                if (counter.get(nums[left]) == 0) {
                    counter.remove(nums[left]);
                }
                left++;
                count += n - right;
            }
            right++;
        }
        return count;        
    }
}
