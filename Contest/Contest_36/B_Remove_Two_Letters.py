t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    doubles = 0
    for i in range(n-2):
        if s[i] == s[i+1]:
            doubles += 1

    print(f'{n} >> {doubles}')