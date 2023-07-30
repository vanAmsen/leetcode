class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int n = nums.size();
        int distinct_elements = unordered_set<int>(nums.begin(), nums.end()).size();
        int count = 0;
        int left = 0;
        int right = 0;
        unordered_map<int, int> counter;

        while (right < n) {
            counter[nums[right]]++;
            while (counter.size() == distinct_elements) {
                if (--counter[nums[left]] == 0) {
                    counter.erase(nums[left]);
                }
                left++;
                count += n - right;
            }
            right++;
        }
        return count;        
    }
};
