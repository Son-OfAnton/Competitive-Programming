n = int(input())
arr = list(map(int, input().split()))

strength = {
    "chest": 0,
    "biceps": 0,
    "back": 0,
}

chest = biceps = back = 0
for i, rep in enumerate(arr):
    turn = i % 3

    if turn == 0:
        strength["chest"] += rep
    elif turn == 1:
        strength["biceps"] += rep
    else:
        strength["back"] += rep

strong = max(strength.values())
for key, val in strength.items():
    if val == strong:
        print(key)
        break