class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> combination(k);
        generateCombinations(1, n, k, combination, result);
        return result;
    }

private:
    void generateCombinations(int start, int n, int k, vector<int> &combination, vector<vector<int>> &result) {
        if (k == 0) {
            result.push_back(combination);
            return;
        }
        for (int i = start; i <= n; ++i) {
            combination[combination.size() - k] = i;
            generateCombinations(i + 1, n, k - 1, combination, result);
        }
    }
};
