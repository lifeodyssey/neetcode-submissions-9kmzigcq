class Solution:

    def encode(self, strs: List[str]) -> str: 
        result=""    
        for s in strs:
            result=result+str(len(s))+"#"+s
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  
        while i < len(s):
            j = i 
            while j < len(s) and s[j] != '#': 
                j += 1
            if j == len(s): 
                break 
            length = int(s[i:j])    
            actual_str = s[j+1 : j+1+length]
            result.append(actual_str)           
            i = j + 1 + length
            
        return result
