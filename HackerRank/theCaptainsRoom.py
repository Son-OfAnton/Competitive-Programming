k = int(input())
rooms = str(input()).split(' ')
room_count = {}

for room in rooms:
    room_count[room] = room_count.get(room, 0) + 1

for room in rooms:
    if room_count.get(room) == 1:
        print(room)
