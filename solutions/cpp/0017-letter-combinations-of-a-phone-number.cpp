class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        if (digits.empty()) return {};

        std::string phone_map[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        std::vector<std::string> output;
        backtrack("", digits, phone_map, output);
        return output;
    }

private:
    void backtrack(std::string combination, std::string next_digits, std::string phone_map[], std::vector<std::string>& output) {
        if (next_digits.empty()) {
            output.push_back(combination);
        } else {
            std::string letters = phone_map[next_digits[0] - '2'];
            for (char letter : letters) {
                backtrack(combination + letter, next_digits.substr(1), phone_map, output);
            }
        }
    }
};
