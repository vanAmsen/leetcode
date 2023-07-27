class Solution {
public:
    string reverseVowels(string s) {
        int start = 0, end = s.size() - 1;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        
        while (start < end) {
            if (vowels.count(s[start]) && vowels.count(s[end])) {
                swap(s[start++], s[end--]);
            } else if (vowels.count(s[start])) {
                end--;
            } else {
                start++;
            }
        }
        return s;
    }
};
