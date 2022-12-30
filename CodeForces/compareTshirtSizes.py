# https://codeforces.com/problemset/problem/1741/A

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    tshirts = input().split()
    tshirt_1 = tshirts[0]
    tshirt_2 = tshirts[1]
    rank = {'L': 3, 'M': 2, 'S': 1}
    
    if rank[tshirt_1[-1]] > rank[tshirt_2[-1]]:
        print(">")
    elif rank[tshirt_1[-1]] < rank[tshirt_2[-1]]:
        print("<")
    else:
        if len(tshirt_1) > len(tshirt_2) and tshirt_1[-1] == 'L':
            print(">")
        elif len(tshirt_1) > len(tshirt_2) and tshirt_1[-1] == 'S':
            print("<")
        elif len(tshirt_1) < len(tshirt_2) and tshirt_1[-1] == 'L':
            print("<")
        elif len(tshirt_1) < len(tshirt_2) and tshirt_1[-1] == 'S':
            print(">")
        else:
            print("=")
