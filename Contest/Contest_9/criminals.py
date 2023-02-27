# https://codeforces.com/gym/429319/problem/B

no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    no_of_rooms = int(input())
    evilness = list(map(int, input().split()))
    
    summ = 0
    non_zero_found = False
    no_of_zeroes = 0

    for index in range(no_of_rooms - 1):
        if evilness[index] != 0:
            non_zero_found = True
            summ += evilness[index]
        else:
            if non_zero_found:
                no_of_zeroes += 1

    print(summ + no_of_zeroes)
    
