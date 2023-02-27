# https://codeforces.com/gym/429319/problem/A

t = int(input())

for _ in range(t):
    no_of_soldiers, iterations = list(map(int, input().split()))
    soldiers = list(input())

    for i in range(min(iterations, no_of_soldiers)):
        to_be_converted = []

        for j in range(no_of_soldiers):
            if j == 0:
                if soldiers[j+1] == '1':
                    to_be_converted.append(j)
            elif j == no_of_soldiers - 1:
                if soldiers[j-1] == '1':
                    to_be_converted.append(j)
            else:
                if (soldiers[j-1] == '1') ^ (soldiers[j+1] == '1'):
                    to_be_converted.append(j)

        for index in to_be_converted:
            soldiers[index] = '1'


    print("".join(soldiers))


