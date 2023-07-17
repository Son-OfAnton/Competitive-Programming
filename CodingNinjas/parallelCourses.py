from collections import defaultdict, deque


def min_semester_finder(n, p):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for _ in range(p):
        pre, course = map(int, input().split())
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque()
    for course in range(1, n+1):
        if indegree[course] == 0:
            queue.append(course)

    min_semester = 0
    courses_taken = 0
    while queue:
        courses_taken += len(queue)
        for _ in range(len(queue)):
            pre = queue.popleft()

            for dep in graph[pre]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)

        min_semester += 1

    return min_semester if courses_taken == n else -1


t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    min_semester = min_semester_finder(n, p)
    print(min_semester)
