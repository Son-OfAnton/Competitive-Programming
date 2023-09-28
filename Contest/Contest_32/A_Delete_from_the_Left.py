word_1 = input()
word_2 = input()
ptr_1, ptr_2 = len(word_1) - 1, len(word_2) - 1

while ptr_1 >= 0 and ptr_2 >= 0 and word_1[ptr_1] == word_2[ptr_2]:
    ptr_1 -= 1
    ptr_2 -= 1

print(ptr_1 + ptr_2 + 2)
