
def find_max(m, s):
    if s == 0:
        return ['0'] if m == 1 else ['-1']
    if s > 9*m:
        return ['-1']

    res = [0]*m
    for i in range(m):
        if s >= 9:
            res[i] = 9
            s -= 9
        else:
            res[i] = s
            s = 0

    return list(map(str, res))


def find_min(max_num):
    min_num = max_num[::-1]

    i = 0
    while min_num[i] == '0':
        i += 1

    min_num[i] = str(int(min_num[i]) - 1)
    min_num[0] = str(int(min_num[0]) + 1)

    return min_num


if __name__ == '__main__':
    m, s = map(int, input().split())
    max_num = find_max(m, s)
    if max_num == ['0'] or max_num == ['-1']:
        print(int(max_num[0]), int(max_num[0]))
        exit()
    min_num = find_min(max_num)


    min_num = int(''.join(min_num))
    max_num = int(''.join(max_num))

    print(min_num, max_num)
