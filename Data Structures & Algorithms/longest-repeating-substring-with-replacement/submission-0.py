class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount=0
        charCount=defaultdict(int) 
        left=0
        n=len(s)
        for right in range(n):
            charCount[s[right]] += 1
            maxCount = max(maxCount, charCount[s[right]])
            while (right-left+1-maxCount)>k:
                charCount[s[left]]-=1
                left+=1
        return  max(maxCount, right - left + 1)
