
'''
백트래킹 : 가능한 모든 방법을 탐색한다
현재 상태에서 가능한 모든 후보군을 따라 들어가며 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고
판단되면 즉시 후보를 포기하면서 정답을 찾아가는 범용적인 알고리즘(가지치기 : Purning)
--> DFS의 비효율적인 경로를 차단하고 목표지점에 갈 수 있는 가능성이 있는 루트를 검사하는 방법
'''
def n_and_m(depth, n, m):
    if depth == m:
        print(''.join(map(str, answer)))

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            n_and_m(depth+1, n, m)
            visited[i] = False
            answer.pop()

n, m = map(int, input().split())
visited = [False] * (n+1)
answer = []

n_and_m(0, n, m)