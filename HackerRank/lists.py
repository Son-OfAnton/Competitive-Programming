# https://www.hackerrank.com/challenges/python-lists?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    arr = []
    commands = []
    
    for i in range(N):
        commands.append(list(input().split()))
    
    for command in commands:
        if "insert" in command:
            arr.insert(int(command[-2]), int(command[-1]))
        elif "print" in command:
            print(arr)
        elif "remove" in command:
            arr.remove(int(command[-1]))
        elif "append" in command:
            arr.append(int(command[-1]))
        elif "sort" in command:
            arr.sort()
        elif "pop" in command:
            arr.pop()
        elif "reverse" in command:
            arr.reverse()
