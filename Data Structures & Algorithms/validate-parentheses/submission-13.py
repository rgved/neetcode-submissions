class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        checkBrack={')':'(', ']':'[','}':'{'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' or i == ']' or i == '}':
                if len(stack)==0:
                    return False
                else:
                    if stack[-1] == checkBrack[i]:
                        stack.pop()
                    else:
                        return False
            else:
                False

        return len(stack)==0
                    
            
        