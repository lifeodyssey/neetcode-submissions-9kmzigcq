class Solution:
    def isValid(self, s: str) -> bool:
        close_of={"(":")","{":"}","[":"]"}
        if len(s)==1:
            return False
        stack=[]
        for char in s:
            if char in close_of:
                stack.append(char)
            if not stack:
                return False
            if char in close_of.values():
                left=stack.pop()
                if close_of[left]!=char:
                    return False
        if not stack:
            return True
        else:
            return False