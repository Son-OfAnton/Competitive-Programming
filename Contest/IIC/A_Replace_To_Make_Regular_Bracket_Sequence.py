seq = input()
match = {'(': {'>', '}', ']'},
         '[': {')', '>', '}'},
         '{': {')', '>', ']'},
         '<': {')', '}', ']'}
        }

exact_match = {'(': ')', '[': ']', '{': '}', '<': '>'}
stack = []


replacement = 0
for char in seq:
    if stack and stack[-1] in exact_match and char == exact_match[stack[-1]]:
        stack.pop()
    elif stack and stack[-1] in match and char in match[stack[-1]]:
        stack.pop()
        replacement += 1
    else:
        stack.append(char)

print('Impossible' if len(stack) > 0 else replacement)