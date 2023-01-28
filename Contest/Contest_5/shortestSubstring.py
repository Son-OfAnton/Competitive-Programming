# https://codeforces.com/gym/424075/problem/C


t = int(input())

for _ in range(t):
    s = input()
    char_count = {'1': 0, '2': 0, '3': 0}
    min_length = float('inf')
    left = 0
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        while all(char_count.values()):
            min_length = min(min_length, right - left + 1)
            char_count[s[left]] -= 1
            left += 1
            
    if min_length == float('inf'):
        print(0)
    else:
        print(min_length)
