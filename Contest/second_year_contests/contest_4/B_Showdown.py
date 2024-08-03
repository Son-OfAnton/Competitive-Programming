t = int(input())

for _ in range(t):
    prob = input()
    a, b = 0, 0
    rem = 10
    i = 0

    while i < 10:
        rem -= 1

        if i % 2 == 0 and prob[i] != '0':
            a += 1
        elif i % 2 == 1 and prob[i] != '0':
            b += 1
        i += 1

        if max(a, b) - min(a, b) + 1 > rem:
            break


    print(i+1)
