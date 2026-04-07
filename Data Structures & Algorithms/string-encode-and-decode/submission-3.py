class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append('#')
            parts.append(s)
        return ''.join(parts)


    def decode(self, s: str) -> List[str]:
        decodedList=[]
        length=len(s)
        i=0
        while i < length:
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            start = j + 1
            end = start + l
            decodedList.append(s[start:end])
            i = end

        return decodedList