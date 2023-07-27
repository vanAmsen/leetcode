public class Solution {
    public String reverseVowels(String s) {
        int start = 0, end = s.length() - 1;
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        char[] arr = s.toCharArray();

        while (start < end) {
            if (vowels.contains(arr[start]) && vowels.contains(arr[end])) {
                char temp = arr[start];
                arr[start++] = arr[end];
                arr[end--] = temp;
            } else if (vowels.contains(arr[start])) {
                end--;
            } else {
                start++;
            }
        }
        return new String(arr);
    }
}
