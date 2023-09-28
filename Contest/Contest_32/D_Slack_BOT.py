def max_similarity(s_1, s_2):
    min_len = min(len(s_1), len(s_2))
    for i in range(min_len):
        if s_1[i] != s_2[i]:
            return i
    return min_len

n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

for i in range(n):
    max_similar_idx = max([max_similarity(strings[i], strings[j]) for j in range(n) if j != i])
    print(max_similar_idx)
