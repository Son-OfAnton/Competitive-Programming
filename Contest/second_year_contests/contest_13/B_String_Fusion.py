class TrieNode:

    def __init__(self):

        self.is_end = False
        self.children = dict()
        self.end_count = 0


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
        curr.end_count += 1

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        common = 0
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False, common
            curr = curr.children[char]
            common += curr.end_count

        return True, common


n = int(input())
trie = Trie()
words = []

for _ in range(n):
    word = input()
    words.append(word)
    trie.insert(word[::-1])

res = 0
for word in words:
    _, common = trie.startsWith(word)
    res += len(word) + 
    res += common

print(res)
