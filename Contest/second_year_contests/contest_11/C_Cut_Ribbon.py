n, a, b, c = map(int, input().split())

max_pieces = 0
for i in range(n//a + 1):
    for j in range((n - i * a) // b + 1):
        rem = n - i * a - j * b

        if rem % c == 0:
            k = rem // c
            max_pieces = max(max_pieces, i + j + k)

print(max_pieces)



