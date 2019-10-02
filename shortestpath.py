N, M = map(int, input().split())
path = [[0 for i in range(N)] for j in range(M)]

for i in range(M):
    for j in range(N):
        if i==0 or j==0:
            path[i][j] = 1
        else:
            path[i][j] = path[i-1][j] + path[i][j-1]

print(path[M-1][N-1])
