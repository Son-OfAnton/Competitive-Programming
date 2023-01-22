# https://codeforces.com/gym/422945/problem/B

number_of_laptops = int(input())
laptops = []

for i in range(number_of_laptops):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

laptops.sort()

for i in range(1, number_of_laptops):
    if laptops[i][0] > laptops[i-1][0] and laptops[i][1] < laptops[i-1][1]:
        print("Happy Alex")
        exit()
print("Poor Alex")



# After sorting the list of tuples by price, if there exist two laptops
# where the first's price is larger than the second but their quality rank 
# is the reverse, the sorting guarantees us to fing them adjacent.

    
