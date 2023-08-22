class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        freq_counter = {} 

        for char in s: 
            freq_counter[char] = freq_counter.get(char, 0) + 1 

        for char in t: 
            if char not in freq_counter: 
                return False 
            freq_counter[char] -= 1 
            if freq_counter[char] == 0: 
                del freq_counter[char] 

        return not freq_counter 
                                                                                                                                                                            
