class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength=0
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                currentString=s[i:j+1]
                length=len(currentString)
                frequencyDict=defaultdict(int)
                for char in currentString:
                    frequencyDict[char]+=1
                maxFrequency=max( freq for freq in frequencyDict.values())
                if length-maxFrequency<=k:
                    maxLength=max(maxLength,length)
        return maxLength