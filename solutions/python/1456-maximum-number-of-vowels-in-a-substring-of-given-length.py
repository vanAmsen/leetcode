class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') 

        # Count vowels in the first window 
        curr_count = sum(1 for char in s[:k] if char in vowels) 
        max_count = curr_count 

        # Slide the window 
        for i in range(k, len(s)): 
            if s[i] in vowels: 
                curr_count += 1 
            if s[i - k] in vowels: 
                curr_count -= 1 

            max_count = max(max_count, curr_count) 

        return max_count 
                                                                                                                                                                        
