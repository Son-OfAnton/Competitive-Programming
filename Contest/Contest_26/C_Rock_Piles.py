dp = dict()

def solve(pa, pb, turn):
    if pa == 0 and pb == 0:
        return not turn
    if (pa, pb, turn) not in dp:
        # ch1 = ch2 = ch3 = None
        res = False
        if pa > 0:
            res |= solve(pa-1, pb, not turn)
        if pb > 0:
            res |= solve(pa, pb-1, not turn)
        if pa > 0 and pb > 0:
            res |= solve(pa-1, pb-1, not turn)
        # if ch1 != None: res |= ch1
        # if ch2 != None: res |= ch2
        # if ch3 != None: res |= ch3

        dp[(pa, pb, turn)] = res

    return dp[(pa, pb, turn)]

t = int(input())

for _ in range(t):
    pa, pb = map(int, input().split())
    winner = solve(pa, pb, True)
    print('hasan' if winner else 'abdullah')