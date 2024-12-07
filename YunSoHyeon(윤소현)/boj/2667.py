size_of_map = int(input())
exist = []

for _ in range(size_of_map):
    exist.append(list(map(int, input())))

visit = [[0 for _ in range(size_of_map)] for _ in range(size_of_map)]
cnt = 0
size_of_complex = []

def DFS(row, col):
    if visit[row][col] == 0:
        visit[row][col] = 1
        if exist[row][col] == 1:
            size_of_complex[cnt - 1] += 1
            if row > 0 and visit[row - 1][col] == 0:
                DFS(row - 1, col)
            if col > 0 and visit[row][col - 1] == 0:
                DFS(row, col - 1)
            if row < size_of_map - 1 and visit[row + 1][col] == 0:
                DFS(row + 1, col)
            if col < size_of_map - 1 and visit[row][col + 1] == 0:
                DFS(row, col + 1)

for i in range(size_of_map):
    for j in range(size_of_map):
        if visit[i][j] == 0 and exist[i][j] == 1:
            size_of_complex.append(0)
            cnt += 1
        DFS(i, j)

print(cnt)
size_of_complex.sort()
print(*size_of_complex, sep='\n')
