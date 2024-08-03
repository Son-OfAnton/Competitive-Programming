row, col = map(int, input().split())

is_ISO_standard = True
prev_color = None

for _ in range(row):
    curr_row = input()
    
    if len(set(curr_row)) > 1:
        is_ISO_standard = False
        break
    if prev_color is not None and prev_color == curr_row[0]:
        is_ISO_standard = False
        break
    prev_color = curr_row[0]

print('YES' if is_ISO_standard else 'NO')