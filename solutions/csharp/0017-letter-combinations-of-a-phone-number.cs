public class Solution {
    public IList<string> LetterCombinations(string digits) {
        if (string.IsNullOrEmpty(digits)) return new List<string>();

        string[] phone_map = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<string> output = new List<string>();
        Backtrack("", digits, phone_map, output);
        return output;
    }

    private void Backtrack(string combination, string next_digits, string[] phone_map, List<string> output) {
        if (next_digits.Length == 0) {
            output.Add(combination);
        } else {
            string letters = phone_map[next_digits[0] - '2'];
            foreach (char letter in letters) {
                Backtrack(combination + letter, next_digits.Substring(1), phone_map, output);
            }
        }
    }
}
