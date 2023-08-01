public class Solution {
    public string ReverseWords(string s) {
        string[] words = s.Trim().Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
        Array.Reverse(words);
        
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < words.Length; i++) {
            result.Append(words[i]);
            if (i < words.Length - 1) result.Append(" ");
        }
        
        return result.ToString();
    }
}
