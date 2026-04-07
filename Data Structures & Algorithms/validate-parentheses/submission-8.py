class Solution:
    def isValid(self, s: str) -> bool:
        pair1=('(',')')
        pair2=('{','}')
        pair3=('[',']')
        openBrackets=['(','{','[']
        closeBrackts=[')','}',']']
        n=len(s)
        if n%2 !=0:
            return False
        stack=[]
        for char in s:
            if char in openBrackets:
                stack.append(char)
            elif char in closeBrackts:
                if not stack:
                    return False
                leftBrackets=stack.pop()
                if ((leftBrackets,char) ==pair1 or (leftBrackets,char) ==pair2 or (leftBrackets,char) ==pair3):
                    continue
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True
