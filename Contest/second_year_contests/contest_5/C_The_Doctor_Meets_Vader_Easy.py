from bisect import bisect_left

spaceships, bases = map(int, input().split())   
attacking_powers = list(map(int, input().split()))
defending_powers = []

for _ in range(bases):
    defending_power, gold = map(int, input().split())
    defending_powers.append([defending_power, gold])

defending_powers.sort()
gold_deposit = []
for i in range(bases):
    gold_deposit.append(defending_powers[i][1])
    defending_powers[i] = defending_powers[i][0]

for i in range(1, bases):
    gold_deposit[i] += gold_deposit[i-1]


for attacking_power in attacking_powers:
    idx = bisect_left(defending_powers, attacking_power)
    
    if idx > 0:
        if idx == bases or defending_powers[idx] != attacking_power:
            res = gold_deposit[idx-1]
            print(res, end=' ')
        else:
            res = gold_deposit[idx]
            print(res, end=' ')
    else:
        print(0, end=' ')
    