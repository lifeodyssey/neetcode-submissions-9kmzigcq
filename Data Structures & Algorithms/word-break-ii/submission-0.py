class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet=set(wordDict)
        memo={}
        def dfs(start:int)->List[str]:
            if start in memo:
                return memo[start]
            if start==len(s):
                return [""]
            res=[]

            for end in range(start+1,len(s)+1):
                word=s[start:end]

                if word in wordSet:
                    suffix_sentences=dfs(end)

                    for suffix in suffix_sentences:
                        if suffix=="":
                            res.append(word)
                        else:
                            res.append(word+" "+suffix)
            memo[start]=res
            return res
        return dfs(0)