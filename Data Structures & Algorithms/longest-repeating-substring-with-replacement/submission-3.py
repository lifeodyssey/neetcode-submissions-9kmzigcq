class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            freq=defaultdict(int)
            maxFreq=0
            for j in range(i,n):
                ch=s[j]
                freq[ch]+=1
                if freq[ch]>maxFreq:
                    maxFreq=freq[ch]
                length=j-i+1
                if length-maxFreq<=k:
                    ans=max(ans,length)
        return ans