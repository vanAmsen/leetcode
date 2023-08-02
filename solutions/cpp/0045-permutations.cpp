class Solution {
public:
    void permuteRec(vector<int>& nums, int begin, vector<vector<int>>& result) { 
            if (begin == nums.size()) { 
                        result.push_back(nums); 
            return; 
            } 
        for (int i = begin; i < nums.size(); i++) { 
            swap(nums[begin], nums[i]); 
            permuteRec(nums, begin + 1, result); 
            swap(nums[begin], nums[i]); 
        } 
    } 
                                                                                                   
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result; 
        permuteRec(nums, 0, result); 
        return result; 
                             
    }
};
