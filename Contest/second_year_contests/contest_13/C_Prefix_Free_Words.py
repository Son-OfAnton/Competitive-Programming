class TrieNode:
    
    def __init__(self):
        
        self.is_end = False
        self.children = dict()
        self.is_leaf = False

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

n = int(input())    
lens = list(map(int, input().split()))

def generate_all_str(k, prefix, all_str):
    if k == 0:
        all_str.append(''.join(prefix))
        return
    
    prefix.append('0')
    generate_all_str(k-1, prefix, all_str)
    prefix[-1] = '1'
    generate_all_str(k-1, prefix, all_str)
    prefix.pop()

trie = Trie()

for l in lens:
    all_str = []
    generate_all_str(l, [], all_str)

    for s in all_str:
        trie.insert(s)
