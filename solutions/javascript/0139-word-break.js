/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let n = s.length;
    let dp = new Array(n + 1).fill(false);
    dp[0] = true;
    let max_len = Math.max(...wordDict.map(word => word.length));

    for (let i = 1; i <= n; i++) {
        for (let j = i - 1; j >= Math.max(i - max_len - 1, 0); j--) {
            if (dp[j] && wordDict.includes(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
};
