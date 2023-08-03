/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length === 0) return [];

    const phone_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
    const output = [];
    backtrack("", digits, phone_map, output);
    return output;

    function backtrack(combination, next_digits, phone_map, output) {
        if (next_digits.length === 0) {
            output.push(combination);
        } else {
            const letters = phone_map[next_digits[0] - '2'];
            for (const letter of letters) {
                backtrack(combination + letter, next_digits.slice(1), phone_map, output);
            }
        }
    }
};
