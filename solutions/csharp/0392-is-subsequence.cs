public class Solution {
    public bool IsSubsequence(string s, string t) {
        int j = 0;
        for (int i = 0; i < t.Length && j < s.Length; i++) {
            if (t[i] == s[j]) {
                j++;
            }
        }
        return j == s.Length;
    }
}
