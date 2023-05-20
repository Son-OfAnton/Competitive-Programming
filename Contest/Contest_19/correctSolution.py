# https://codeforces.com/gym/443238/problem/A

question = list(input())
bob_answer = list(input())
right_answer = sorted(question)

if len(bob_answer) != len(right_answer):
    print('WRONG_ANSWER')
    exit()

if right_answer[0] == '0' and len(right_answer) > 1:
    ptr = 0
    while ptr < len(right_answer) and right_answer[ptr] == '0':
        ptr += 1
    right_answer[ptr], right_answer[0] = right_answer[0], right_answer[ptr]

if int(''.join(bob_answer)) == int(''.join(right_answer)):
    print('OK')
else:
    print('WRONG_ANSWER')
