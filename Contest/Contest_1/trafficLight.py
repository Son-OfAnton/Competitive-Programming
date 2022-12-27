n = int(input())

for i in range(n):
    test_cases = list(input().split())
    current_light = test_cases[1]
    lights = 2*input()
    res = 0
    left = 0
    right = 0

    while right < len(lights):

        while right < len(lights)  and  lights[right] != current_light:
            right+=1
        left = right

        while right < len(lights) and lights[right] != 'g':
            right+=1

        res = max(res, right-left)
        right+=1


    print(res)
