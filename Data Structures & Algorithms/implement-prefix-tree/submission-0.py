class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
class PrefixTree:
    
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.isEnd=True

    def search(self, word: str) -> bool:
        node=self.findNode(word)
        if not node:
            return False
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None
    
    def findNode(self,s:str):
        node=self.root
        for char in s:
            if char not in node.children:
                return None
            node=node.children[char]
        return node
        