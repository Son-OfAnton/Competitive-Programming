n = int(input())
tv_programs = [tuple(map(int, input().split())) for _ in range(n)]

schedule = []
for start, end in tv_programs:
    schedule.append((start, 1))
    schedule.append((end + 1, -1))

schedule.sort()

tv_needed = 0
for event_time, event_type in schedule:
    tv_needed += event_type
    if tv_needed > 2:
        print("NO")
        break
else:
    print("YES")
