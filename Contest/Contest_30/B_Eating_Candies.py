from itertools import accumulate


t = int(input())

for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))

    alice = list(accumulate(candies))
    bob = list(accumulate(candies[::-1]))

    alice_map, bob_map = dict(), dict()
    res = 0
    for i, num in enumerate(alice):
        alice_map[num] = i+1
    for  i, num in enumerate(bob):
        if num in alice_map and alice_map[num] < n - i:
            res = alice_map[num] + i+1
        bob_map[num] = i+1

    print(res)




    """
    
    2 1 4 2 4 1

    2 3 7 9 13 14
    14 12 11 7 5 1


    7 3 20 5 15 1 11 8 10

    7 10 30 35 50 51 62 70 80
    80 73 70 50 45 30 29 18 10


    """