def test_01_knapsack():
    n = 3
    val = [1,2,3]
    weights = [4,5,1]
    capacity = 3
    dp = dict()

    def knapsack(i, capacity):
        if i == n:
            return 0
        if (i, capacity) in dp:
            return dp[(i, capacity)]
        if weights[i] > capacity:
            return knapsack(i+1, capacity)
                
        no_pick = knapsack(i+1, capacity)
        pick = val[i] + knapsack(i+1, capacity - weights[i])
        dp[(i, capacity)] = max(pick, no_pick)

        return dp[(i, capacity)]
            
    print("Maximum profit is :", end=" ")
    print(knapsack(0, capacity))


def test_unbounded_knapsack():
    n = 3
    val = [1,2,3]
    weights = [3,2,1]
    capacity = 3
    dp = dict()

    def unbounded_knapsack(i, capacity):
        if i == n-1:
            return (capacity // weights[n-1]) * val[n-1]
        if (i, capacity) in dp:
            return dp[(i, capacity)]
        if weights[i] > capacity:
            return unbounded_knapsack(i+1, capacity)
                
        no_pick = unbounded_knapsack(i+1, capacity)
        pick = val[i] + unbounded_knapsack(i, capacity - weights[i])
        dp[(i, capacity)] = max(pick, no_pick)

        return dp[(i, capacity)]
            
    print("Maximum profit is :", end=" ")
    print(unbounded_knapsack(0, capacity))

# test_unbounded_knapsack()
test_01_knapsack()