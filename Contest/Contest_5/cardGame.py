# https://codeforces.com/gym/424075/problem/A

arr_size = int(input())
cards = list(map(int, input().split()))

left = 0
right = arr_size - 1
wube = 0
henok = 0
wube_turn = True

while left <= right:
    if wube_turn:
        if cards[left] > cards[right]:
            wube += cards[left]
            left += 1
        else:
            wube += cards[right]
            right -= 1
        wube_turn = False
    if left <= right and  not wube_turn:
        if cards[left] > cards[right]:
            henok += cards[left]
            left += 1
        else:
            henok += cards[right]
            right -= 1
        wube_turn = True
        
            
print(f"{wube} {henok}")
