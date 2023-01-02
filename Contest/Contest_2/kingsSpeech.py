# https://codeforces.com/gym/419351/problem/A

word_num = int(input())

for i in range(word_num):
    word = input()
    print(word[0:2] + "... " + word + "?")
