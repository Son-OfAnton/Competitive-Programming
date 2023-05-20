from collections import defaultdict


t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    orbits = map(int, input().split())
    orbit_map = defaultdict(list)

    cost = 0
    for i, orbit in enumerate(orbits):
        orbit_map[orbit].append(i)

    for group in orbit_map:
        if len(orbit_map[group]) != 0:
            cost += min((len(orbit_map[group]), c))
       
    print(cost)
