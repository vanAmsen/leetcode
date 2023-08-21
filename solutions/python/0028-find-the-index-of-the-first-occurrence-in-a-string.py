class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: 
            return 0 

        if not haystack or len(haystack) < len(needle): 
            return -1 

        for i in range(len(haystack) - len(needle) + 1): 
            if haystack[i:i+len(needle)] == needle: 
                return i 

        return -1 
                                                                                                                            
