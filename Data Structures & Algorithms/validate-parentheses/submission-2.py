class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in {'{', '(', '['}:
                stack.append(char)
            elif len(stack) == 0:
                    return False
            elif char == '}':
                top_item = stack.pop()
                if top_item != '{':
                    return False
            
            elif char == ']':
                top_item = stack.pop()
                if top_item != '[':
                    return False
            
            elif char == ')':
                top_item = stack.pop()
                if top_item != '(':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
