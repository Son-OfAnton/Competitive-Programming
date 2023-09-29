class TrieNode:
    def __init__(self):
        self.children = dict()
        self.val = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_num(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit_val = 1 if num & (1 << i) else 0
            if bit_val not in curr.children:
                curr.children[bit_val] = TrieNode()
            curr = curr.children[bit_val]
        curr.val = num

    def find_max_xor(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0
            opposite_bit = 1 - bit
            if opposite_bit in curr.children:
                curr = curr.children[opposite_bit]
            else:
                curr = curr.children[bit]

        return curr.val if curr.val is not None else 0


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        bit_trie = Trie()

        for num in nums:
            bit_trie.add_num(num)

        max_xor = 0
        for num in nums:
            best_xor_pair = bit_trie.find_max_xor(num)
            max_xor = max(max_xor, best_xor_pair ^ num)

        print(max_xor)


if __name__ == "__main__":
    solve()
