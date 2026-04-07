class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        ans=0
        n=len(s)
        for right in range(n):
            char=s[right]
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(char)
            ans=max(ans,len(seen))
        return ans
