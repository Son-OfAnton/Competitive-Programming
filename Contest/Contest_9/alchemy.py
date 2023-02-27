# https://codeforces.com/gym/429319/problem/C

no_of_ingredients = int(input())
ingredients = list(map(int, input().split()))

edward, alphonse = 0, 0 

prefix = [ingredients[0]]
for i in range(1, no_of_ingredients):
    prefix.append(prefix[-1] + ingredients[i])

postfix = [ingredients[-1]]
for i in range(no_of_ingredients - 2, -1, -1):
    postfix.append(postfix[-1] + ingredients[i])

for i in range(no_of_ingredients):
    if prefix[i] <= postfix[no_of_ingredients - i - 1]:
        edward += 1
    else:
        alphonse += 1

print(f'{edward} {alphonse}')
