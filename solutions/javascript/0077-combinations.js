/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    const result = [];
    generateCombinations(1, n, k, [], result);
    return result;
};

function generateCombinations(start, n, k, combination, result) {
    if (k === 0) {
        result.push([...combination]);
        return;
    }
    for (let i = start; i <= n; ++i) {
        combination.push(i);
        generateCombinations(i + 1, n, k - 1, combination, result);
        combination.pop();
    }
}
