from heapq import heappush, heappop
t = int(input())

for _ in range(t):
    n = int(input())
    box = list(map(int, input()))
    mag = list(map(int, input().split()))
    lids = box.count(1)
    last_count = mag.count(mag[-1])

    # if lids == 1 and n == 1:
    #     print(1)
    #     continue


    new_mag = []
    for i, val in enumerate(mag):
        new_mag.append([val, i])
    # print(new_mag)
    # new_mag = mag[:]
    new_mag.sort(reverse=True)
    max_saved_mags = 0
    i = 0
    while lids > 0 and i < n - 1:
        # print(new_mag[i])
        index = new_mag[i][1]
        if index > 0:
            if (mag[index-1] == 1 or mag[index+1] == 0) and new_mag[i][0] != mag[-1] or n == 1:
                max_saved_mags += new_mag[i][0]
                lids -= 1
            else:
                if last_count > 1:
                    max_saved_mags += new_mag[i]
                    lids -= 1
                    last_count -= 1

        i += 1

    if mag[0] == 1:
        max_saved_mags += 1

    print(max_saved_mags)




