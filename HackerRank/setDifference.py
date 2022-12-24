# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

english_students_num = int(input())
english_newspaper = set(input().split())
french_students_num = int(input())
french_newspaper = set(input().split())
res = len(english_newspaper.difference(french_newspaper))

print(res)
