def countingValleys(steps, path):
    # Write your code here
    alt, valleys = 0, 0
    for i in path:
        if i == 'U':
            if alt == -1:
                valleys += 1
            alt += 1
        else:
            alt -= 1
    return valleys
