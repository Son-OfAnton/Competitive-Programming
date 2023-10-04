from collections import defaultdict


q = int(input())
multi = defaultdict(int)
multi[0] += 1

def find_max_xor(num):
    res = 0
    for ele in multi:
        res = max(res, num ^ ele)

    return res

for _ in range(q):
    op, arg = input().split()
    if op == '+':
        multi[int(arg)] += 1
    elif op == '-':
        multi[int(arg)] -= 1
        if multi[int(arg)] == 0:
            del multi[int(arg)]
    else:
        print(find_max_xor(int(arg)))
