# class Union_find:
#     def __init__(self, n):
#         self.rep = list(range(n))
#         self.size = [1] * n 

#     def find(self, x):
#         if x != self.rep[x]:
#             self.rep[x] = self.find(self.rep[x])
#         return self.rep[x]

#     def union(self, x, y):
#         x_rep = self.find(x)
#         y_rep = self.find(y)

#         if self.size[x_rep] < self.size[y_rep]:
#             self.rep[x_rep] = y_rep
#             self.size[y_rep] += self.size[x_rep]
#         else:
#             self.rep[y_rep] = x_rep
#             self.size[x_rep] += self.size[y_rep]

#     def connected(self, x, y):
#         return self.find(x) == self.find(y)

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input()

#     uf = Union_find(26)

def get_prototype_string(t):
    n = len(t)
    s = ['a'] * n
    in_edges = [0] * 26
    out_edges = [0] * 26

    for i in range(n):
        curr = ord(t[i]) - ord('a')
        prev = ord(s[i - 1]) - ord('a') if i > 0 else 0
        diff = (curr - prev) % 26

        # Update the in and out edges
        out_edges[prev] = curr
        in_edges[curr] = prev

        # Check if there is a small circle
        if out_edges[curr] != 0:
            j = curr
            circle_size = 1
            while out_edges[j] != curr and circle_size < 26:
                j = out_edges[j]
                circle_size += 1

            if circle_size < 26:
                # Find the maximum unused letter to break the circle
                for k in range(25, -1, -1):
                    if in_edges[k] == 0 and out_edges[k] == 0:
                        out_edges[curr] = k
                        in_edges[k] = curr
                        break

        # Update the current letter in s
        s[i] = chr(ord('a') + diff)

    return ''.join(s)

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the length of the string t
    n = int(input())

    # Read the string t
    t_str = input()

    # Get the lexicographically smallest string s
    s = get_prototype_string(t_str)

    # Print the result
    print(s)
