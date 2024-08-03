class TrieNode:
    
    def __init__(self):
        
        self.is_end = False
        self.children = dict()
        

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_end 

        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True
