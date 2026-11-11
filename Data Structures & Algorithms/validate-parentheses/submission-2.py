class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
        
        return True if not stack else False

        #how this works is we build our stack as we iterate through the list, and constantly check if the character is an opening or closing brace, if it is a closing brace we check if the most recent addition to the stack is an opening brace of the same type (using the dictionary), if it is the same type we pop from the stack and therefore we then move on to the next bracket.
        #if we get multiple opening brackets in a row we just keep building the stack through appending it once making sure the bracket is not a key in closeToOpen

        #tldr we make sure the brackets close in the opposite order to how they open