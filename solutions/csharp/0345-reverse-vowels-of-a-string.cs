public class Solution {
    public string ReverseVowels(string s) {
        int start = 0, end = s.Length - 1;
        HashSet<char> vowels = new HashSet<char> {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        char[] arr = s.ToCharArray();

        while (start < end) {
            if (vowels.Contains(arr[start]) && vowels.Contains(arr[end])) {
                char temp = arr[start];
                arr[start++] = arr[end];
                arr[end--] = temp;
            } else if (vowels.Contains(arr[start])) {
                end--;
            } else {
                start++;
            }
        }
        return new string(arr);
    }
}
