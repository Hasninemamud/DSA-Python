class Solution(object):
    def isValid(self, s):
        # Stack to keep track of opening brackets
        stack = []
    
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
    
        # Loop through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack (if it is not empty)
                # Otherwise, assign a dummy value '#' which will not match any opening bracket
                top_element = stack.pop() if stack else '#'
            
                # Check if the top element matches the corresponding opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack
                stack.append(char)
        
        # Return True if the stack is empty, otherwise False
        return not stack
s1 = Solution()
print(s1.isValid('{([])}'))
