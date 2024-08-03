string = input()
stack = []

for char in string:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

print("".join(stack))


