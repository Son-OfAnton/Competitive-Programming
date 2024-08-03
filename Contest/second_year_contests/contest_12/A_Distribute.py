n = int(input())
cards = list(map(int, input().split()))

indexed_cards = list(enumerate(cards, 1))
indexed_cards.sort(key=lambda x: x[1])

distribution = []
for i in range(n // 2):
    distribution.append((indexed_cards[i][0], indexed_cards[n-1-i][0]))

for pair in distribution:
    print(*pair)


