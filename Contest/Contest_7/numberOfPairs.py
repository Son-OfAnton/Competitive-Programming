# https://codeforces.com/gym/426940/problem/C

b = int(input())
boys = list(map(int, input().split()))
boys.sort()
g = int(input())
girls = list(map(int, input().split()))
girls.sort()

b_ptr = g_ptr = 0
count = 0

while b_ptr < b and g_ptr < g:
    if abs(boys[b_ptr] - girls[g_ptr]) <= 1:
        count += 1
        b_ptr += 1
        g_ptr += 1
    
    elif boys[b_ptr] - girls[g_ptr] > 1:
        g_ptr += 1
    elif girls[g_ptr] - boys[b_ptr] > 1:
        b_ptr += 1
    elif boys[b_ptr] == girls[g_ptr]:
        if b >= g:
            g_ptr += 1
        else:
            b_ptr += 1
            
print(count)
            
