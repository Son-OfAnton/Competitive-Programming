def countingValleys(steps, path):
    # Write your code here
    altitute, valleys = 0, 0
    for i in path:
        if i == 'U':
            if altitute == -1:
                valleys += 1
            altitute += 1
        else:
            altitute -= 1
    return valleys
