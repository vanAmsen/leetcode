public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        int n = s.Length;
        bool[] dp = new bool[n + 1];
        dp[0] = true;
        int max_len = 0;
        foreach (string word in wordDict) {
            max_len = Math.Max(max_len, word.Length);
        }

        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j >= Math.Max(i - max_len - 1, 0); j--) {
                if (dp[j] && wordDict.Contains(s.Substring(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
}
