class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> count;
        for (int num : arr) {
            count[num]++;
        }
        unordered_set<int> uniqueCount;
        for (auto& pair : count) {
            if (!uniqueCount.insert(pair.second).second) {
                return false;
            }
        }
        return true;
    }
};
