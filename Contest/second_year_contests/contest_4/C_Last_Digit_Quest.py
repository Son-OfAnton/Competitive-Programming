t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(input().split())
    nums = [num[-1] for num in nums]

    comb = {"003", "012", "111", "049", "139", "229", "058", "148",
            "238", "067", "157", "247", "337", "599", "689", "779", "889"}
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                
                if sorted(f'{nums[i]}{nums[j]}{nums[k]}') in comb:
                    print("YES")
                    exit()

    print("NO")

