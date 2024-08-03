def lexicographically_minimal(s):
    count = [0] * 26
    
    # Step 1: Update count array
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    t = []
    answer = ""
    
    # Step 2: Iterate through characters of string s
    for char in s:
        # Step 3: Push the current character onto the stack
        t.append(char)
        
        # Step 4: Pop letters from stack t and append to answer
        while t and (not count[ord(t[-1]) - ord('a')] or t[-1] <= char):
            answer += t.pop()
    
    # Step 5: Append remaining characters from stack t to answer
    while t:
        answer += t.pop()
    
    # Step 6: Return the resulting answer string
    return answer[::-1]  # Reverse the answer string

# Input
s = input()

# Output
print(lexicographically_minimal(s))
