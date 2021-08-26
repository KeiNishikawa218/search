n = int(input())

tree = [[] for _ in range(n+1)]

# ツリーを構築
for _ in range(n):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    tree[a].append(b)
    tree[b].append(a)

isSearched = [False]*(n+1)

def dfs(i):
    if isSearched[i]:
        return 

    print(f'現在探索中のノード: {i+1}')
    isSearched[i] = True

    for node in tree[i]:
        if not isSearched[node]:
            dfs(node)

# 1番目のノードから探索を開始
dfs(0)
