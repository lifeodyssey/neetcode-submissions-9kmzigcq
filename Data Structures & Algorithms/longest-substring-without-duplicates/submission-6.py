class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        maxLength=0
        for left in range(n):
            charSet=set()
            for right in range(left,n):
                if s[right] in charSet:
                    break
                else:
                    charSet.add(s[right])
                    currentLength=right-left+1 
                    maxLength=max(maxLength,currentLength)
        return maxLength