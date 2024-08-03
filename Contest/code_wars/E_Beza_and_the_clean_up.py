
n, m, s, A, B = map(int, input().split())
trash_A = list(map(int, input().split()))
trash_B = list(map(int, input().split()))

trash_A.sort(reverse=True)
trash_B.sort(reverse=True)


i, j = 0, 0

value = 0
total = 0
last_added = None
flag = False

while i < min(n, m) and j < min(n, m):
    # print(f'total {total} value {value} last_added {last_added} i-{i} j-{j}')
    if trash_A[i] > trash_B[j]:
        total += A
        value += trash_A[i]
        i += 1
        last_added = A
    elif trash_A[i] < trash_B[i]:
        value += trash_B[j]
        total += B
        j += 1
        last_added = B
    else:
        if A <= B:
            value += trash_A[i]
            total += A
            last_added = A
        else:
            value += trash_B[j]
            total += B
            last_added = B

    if total == s:
        flag = True
        break
    elif total > s:
        flag = True
        value -= last_added
        break

if not flag:
    while i < n and total < s:
        value += trash_A[i] 
        total += A
        last_added = A
    while j < m and total < s:
        value += trash_B[j] 
        total += B
        last_added = B

    if total > s:
        value -= last_added

    
print(value)