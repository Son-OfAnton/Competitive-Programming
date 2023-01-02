# https://codeforces.com/gym/419351/problem/E

first_line = input().split()
lecture_minute = int(first_line[0])
woke_minute = int(first_line[1])
theorems = list(map(int, input().split()))
behaviors = list(map(int, input().split()))

theorems_by_himself = 0

for index, behavior in enumerate(behaviors):
    if behavior == 1:
        theorems_by_himself += theorems[index]
        theorems[index] = 0

left = 0
right = 0
theorems_by_me = 0
current_total_theorem = 0

while right < lecture_minute:
    while right < left + woke_minute:
        current_total_theorem += theorems[right]
        right += 1

    theorems_by_me = max(theorems_by_me, current_total_theorem)
    current_total_theorem -= theorems[left]
    left += 1

print(theorems_by_me + theorems_by_himself)
