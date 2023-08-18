class Solution:
    def decodeString(self, s: str) -> str:
        num_stack, char_stack = [], [] 
        curr_num = 0 
        curr_str = '' 

        for char in s: 
            if char.isdigit(): 
                curr_num = curr_num * 10 + int(char) 
            elif char == '[': 
                num_stack.append(curr_num) 
                char_stack.append(curr_str) 
                curr_num = 0 
                curr_str = '' 
            elif char == ']': 
                repeat_num = num_stack.pop() 
                prev_str = char_stack.pop() 
                curr_str = prev_str + repeat_num * curr_str 
            else: 
                curr_str += char 

        return curr_str 
                                                                                                                                                                                                                                                                  
