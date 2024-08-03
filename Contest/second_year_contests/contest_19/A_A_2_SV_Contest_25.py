a, b, c, d = map(int, input().split())
paulos_score = max(3*a/10, a - a/250*c)
mighty_score = max(3*b/10, b - b/250*d)

if paulos_score > mighty_score:
    print("Misha")
elif paulos_score < mighty_score:
    print("Vasya")
else:
    print("Tie")