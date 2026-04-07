class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringDict=defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            stringDict[key].append(s)
        return list(stringDict.values())