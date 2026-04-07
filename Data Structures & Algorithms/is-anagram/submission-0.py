class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount={}
        for char in s:
                sCount[char]=sCount.get(char,0)+1
        tCount={}
        for char in t:
                tCount[char]=tCount.get(char,0)+1    
        if sCount==tCount:
            return True
        else:
            return False

    