class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.isEnd=True        

    def search(self, word: str) -> bool:
        def dfs(node:TrieNode,i:int)->bool:
            if i==len(word):
                return node.isEnd
            ch=word[i]
            if ch !='.':
                if ch not in node.children:
                    return False
                return dfs(node.children[ch],i+1)
            for nxt in node.children.values():
                if dfs(nxt,i+1):
                    return True
            return False
        return dfs(self.root,0)
