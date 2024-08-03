n, x, y = map(int, input().split())

t = 0
while True:
    finish_1 = t + x
    finish_2 = t + y

    while True:
        t += 1
        if t == finish_1:
            