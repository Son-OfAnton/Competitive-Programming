# https://codeforces.com/problemset/problem/1611/B

def main():
    test_c = int(input())

    for _ in range(test_c):
        a, b = map(int, input().split())
        left, right = 0, (a + b) // 4
        best = 0

        while left <= right:
            mid = left + (right - left) // 2

            if a - mid >= 0 and b - mid >= 0:
                temp = a - mid  + b - mid
                
                if mid * 2 <= temp:
                    best = mid
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right = mid - 1

        print(best)
            
        
        


if name == 'main':
    main()
