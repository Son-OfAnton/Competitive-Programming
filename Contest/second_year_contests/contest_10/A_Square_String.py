t = int(input())

# for _ in range(t):
#     s = input()
#     n = len(s)

#     if n % 2 == 1:
#         print('NO')

#     for i in range(len(s)//2):

#         if s[i] != s[i + n//2]:
#             print('NO')
#             break
#     else:
#         print('YES')
for _ in range(t):
    s = input()
    half = len(s) // 2
    print('YES' if s[:half] == s[half:] else 'NO')