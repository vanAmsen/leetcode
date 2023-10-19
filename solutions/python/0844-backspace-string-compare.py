class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        
        return process_string(s) == process_string(t)
