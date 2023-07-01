def main(binary):
    suffix_0_count = binary.count('0')
    suffix_1_count = binary.count('1')
    min_op = min(suffix_0_count, suffix_1_count)

    prefix_0_count = 0
    prefix_1_count = 0
    for char in binary:
        if char == '0':
            prefix_0_count += 1
            suffix_0_count -= 1
        else:
            prefix_1_count += 1
            suffix_1_count -= 1

        min_op = min(min_op, prefix_1_count + suffix_0_count)
        min_op = min(min_op, prefix_0_count + suffix_1_count)

    return min_op


t = int(input())

for _ in range(t):
    binary = input()
    min_op = main(binary)
    print(min_op)
