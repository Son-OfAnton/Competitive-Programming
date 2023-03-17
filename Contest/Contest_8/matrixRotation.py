# https://codeforces.com/gym/428168/problem/A

def rotate90(matrix):
    # tranposing
    matrix[0][1], matrix[1][0] = matrix[1][0], matrix[0][1]

    for row in matrix:
        row.reverse()


t = int(input())

for _ in range(t):
    matrix = []
    row_1 = list(map(int, input().split()))
    row_2 = list(map(int, input().split()))
    matrix.append(row_1)
    matrix.append(row_2)
    flag = False

    for op in range(4):
        if matrix[0][0] < matrix[0][1] and matrix[0][0] < matrix[1][0] \
                and matrix[1][0] < matrix[1][1] and matrix[0][1] < matrix[1][1]:
            print("YES")
            flag = True
            break

        rotate90(matrix)

    if not flag:
        print("NO")
