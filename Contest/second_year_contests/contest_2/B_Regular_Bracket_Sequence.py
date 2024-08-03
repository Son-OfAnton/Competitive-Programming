brackets = input()
stack = []
regular_bracket_count = 0

for bracket in brackets:
    if bracket == '(':
        stack.append(bracket)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
            regular_bracket_count += 2

print(regular_bracket_count)