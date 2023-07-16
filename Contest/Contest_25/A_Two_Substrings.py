
s = input()
ptr_1 = s.find("AB")  
ptr_2 = s.find("BA", ptr_1 + 2)  
ptr_3 = s.find("BA")
ptr_4 = s.find("AB", ptr_3 + 2)

if (ptr_1 != -1 and ptr_2 != -1) or (ptr_3 != -1 and ptr_4 != -1):
    print("YES")
else:
    print("NO")

