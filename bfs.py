from collections import deque

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    tree[a].append(b)
    tree[b].append(a)

isSearched = [False]*(n+1)

d = deque([0])

while d:
    v = d.popleft()

    print(f'現在探索中のノード: {v+1}')
    isSearched[v] = True

    for node in tree[v]:
        if not isSearched[node]:
           d.append(node)

