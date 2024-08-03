class TrieNode:

    def __init__(self):

        self.is_end = False
        self.children = dict()
        self.which = []
        self.val = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, tag: int) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                curr.children[char].val = char
                curr.children[char].which.append(tag)
            curr = curr.children[char]
        curr.is_end = True

    # def search(self, word: str) -> bool:
    #     curr = self.root
    #     for char in word:
    #         if char not in curr.children:
    #             return False
    #         curr = curr.children[char]

    #     return curr.is_end

    # def startsWith(self, prefix: str) -> bool:
    #     curr = self.root
    #     for char in prefix:
    #         if char not in curr.children:
    #             return False
    #         curr = curr.children[char]

    #     return True
    

def main():
    s1 = input()
    s2 = input()

    trie = Trie()
    trie.insert(s1, 0)
    trie.insert(s2, 1)
    dummy_root = trie.root

    def dfs(root):
        depth = 0
        while len(root.children) == 1:
            for child in root.children:
                root = child
                depth += 1

        next_1 = None
        for _ in range(2):
            for child in root.children:
                if child.which == 0:
                    next_1 = child
        next_2 = None
        for child in root.children:
            if child.which == 1:
                next_2 = child
                break

        # while next_1.val == next_2.val:
        while next_1 and next_2:
            if next_1.val != next_2.val:
                return False
            flag_1, flag_2 = False, False
            for child in next_1.children:
                flag_1 = True
                next_1 = child
            for child in next_2.children:
                flag_2 = True
                next_2 = child

            if not (flag_1 & flag_2):
                return False
            
        return depth
    
    print(dfs(dummy_root))
        


        
        
        # for child in root.children:
        #     if 
