dic = {}
n = int(input())

for i in range(n):
    entry = str(input())
    dic[entry] = dic.get(entry, 0) + 1    

print(len(dic))
for i in dic.keys():
    print(dic[i], end=" ")
