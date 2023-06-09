class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(' : ')', '[' : ']', '{' : '}'} 

        for c in s:
            if c in brackets.keys():
                stack.append(c)
            else:
                if len(stack) == 0: return False
                o = stack.pop()
                if (c != brackets.get(o)):
                    return False
        return len(stack) == 0
