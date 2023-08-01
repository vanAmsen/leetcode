class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces, reverse the order of words, and then join them back together with a single space
        return ' '.join(s.strip().split()[::-1])
