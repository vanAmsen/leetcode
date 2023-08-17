class Solution:
    def removeStars(self, s: str) -> str:
        stack = [] 

        for char in s: 
            if char != '*': 
                stack.append(char) 
            elif stack: 
                stack.pop() 

        return ''.join(stack) 
                                                                                                                     
