# https://codeforces.com/problemset/problem/1730/A

from collections import Counter

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    planet_num, cost = map(int, input().split())
    orbit = list(map(int, input().split()))
    count = Counter(orbit)
    unique_orbits = set(orbit)
    min_cost = 0
    
    for orbit in unique_orbits:
        min_cost += min(cost, count[orbit])
    
    print(min_cost)
    
    
    
    
