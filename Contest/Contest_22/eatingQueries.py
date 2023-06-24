# https://codeforces.com/gym/450068/problem/B

from bisect import bisect_left

def main():
	t = int(input())

	for _ in range(t):
		n, q = map(int, input().split())
		candies = list(map(int, input().split()))
		candies.sort(reverse=True)

		for i in range(1, n):
			candies[i] += candies[i - 1]

		for _ in range(q):
			curr_query = int(input())
			min_candies = bisect_left(candies, curr_query)
			print(min_candies + 1 if min_candies != n else -1)

main()

