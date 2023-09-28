class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def find_max_xor(self, word):
        curr = self.root
        xor_result = []
        for char in word:
            opposite_bit = '1' if char == '0' else '0'
            if opposite_bit in curr.children:
                xor_result.append(opposite_bit)
                curr = curr.children[opposite_bit]
            else:
                xor_result += char
                curr = curr.children[char]
        return int(''.join(xor_result), 2)


def solve():
    t = int(input())
    num_binary = dict()
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        max_bits_needed = max(nums).bit_length() + 1
        trie = Trie()

        for num in nums:
            binary = bin(num)[2:].zfill(max_bits_needed)
            trie.insert(binary)
            num_binary[num] = binary

        max_xor = 0
        for num in nums:
            binary = num_binary[num]
            best = trie.find_max_xor(binary)
            max_xor = max(max_xor, best ^ num)

        print(max_xor)


if __name__ == "__main__":
    solve()
