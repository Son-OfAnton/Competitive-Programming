number_of_patterns = int(input())
patterns = []

for i in range(number_of_patterns):
    patterns.append(input())

pattern_length = len(patterns[0])
identifier = "?"
result = ""

for i in range(pattern_length):
    for j in range(number_of_patterns):
        if identifier == "?" and ord("a") <= ord(patterns[j][i]) <= ord("z"):
            identifier = patterns[j][i]

        elif identifier != "?" and patterns[j][i] != identifier and patterns[j][i] != "?":
            result += '?'
            identifier = "?"
            break

        if j == number_of_patterns - 1:
            if identifier == '?':
                result += 'x'

            else:
                result += identifier
                identifier = "?"

print(result)
