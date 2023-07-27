# 🔄 Reverse Vowels, Not Consonants! Mastering the Two-Pointer Technique in Python 🐍

# Intuition
When first encountering this problem, it's clear that we need a way to traverse the string and identify the vowels that need to be reversed. Since we only need to reverse the vowels and keep the consonants in their place, a brute force approach of reversing the entire string won't work here. Hence, we'll need a way to traverse from both ends of the string and swap the vowels when we encounter them.

# Approach
The approach we use here is the two-pointer technique, a common technique used in problems involving sequences or linked lists. We start by initializing two pointers, one at the beginning of the string and the other at the end. We move these pointers inward, checking if the characters at these positions are vowels.

If both characters are vowels, we swap them. If the character at the start pointer isn't a vowel, we move the start pointer to the right. If the character at the end pointer isn't a vowel, we move the end pointer to the left. We repeat this process until the two pointers meet, indicating we've checked all characters in the string.

# Complexity
- Time complexity:
The time complexity is \(O(n)\) where \(n\) is the length of the string. This is because we're traversing through the string once.

- Space complexity:
The space complexity is \(O(n)\) because we convert the string to a list, which takes up space. We also have a constant space for storing the vowels set but since we're considering the input size, it's \(O(n)\).

# Code
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU") 
        s = list(s) 
        start, end = 0, len(s) - 1 
        while start < end: 
            if s[start] in vowels and s[end] in vowels: 
                s[start], s[end] = s[end], s[start] 
                start += 1 
                end -= 1 
            elif s[start] not in vowels: 
                start += 1 
            elif s[end] not in vowels: 
                end -= 1 
        return "".join(s) 
```
