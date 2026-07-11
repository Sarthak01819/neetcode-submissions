class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for val in s:
            if val in ['(', '[', '{']:
                res.append(val)
            elif val == ')' and res and res[-1] == '(':
                res.pop()
            
            elif val == ']' and res and res[-1] == '[':
                res.pop()
            
            elif val == '}' and res and res[-1] == '{':
                res.pop()
            else:
                return False

        return len(res) == 0