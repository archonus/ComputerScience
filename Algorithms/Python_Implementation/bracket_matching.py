from collections import deque


open_brackets = {'(': ')', '[': ']', '{': '}'}

def isBalanced(s : str):
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False
    stack = deque()
    if s[0] in open_brackets:
        stack.append(s[0])
    elif s[0] in open_brackets.values():
        return False # Cannot start with closed bracket
    
    for c in s[1:]:  # Skip first
        if c in open_brackets:
            stack.append(c)
        elif c in open_brackets.values(): # Closed bracket
            if len(stack) == 0: # Not expecting anything, so not balanced
                return False
            current = stack.pop()
            if c != open_brackets[current]: # Not one expected
                return False  # Break
    
    
    return len(stack) == 0

if __name__ == "__main__":
    print(isBalanced("())("))