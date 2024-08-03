n = int(input())
heights = list(map(int, input().split()))

energy = 0
dollar = 0
prev_height = 0

for curr_height in heights:
    energy += prev_height - curr_height
    if energy < 0:
        dollar -= energy
        energy = 0
    prev_height = curr_height

print(dollar)
