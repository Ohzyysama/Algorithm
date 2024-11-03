fx = [0, 2, 2, 1, 1, -1, -1, -2, -2]
fy = [0, 1, -1, 2, -2, 2, -2, 1, -1]
board = [[0 for _ in range(30)] for _ in range(30)]
f = [[0 for _ in range(30)] for _ in range(30)]
typein = input().split()
endx = int(typein[0])
endy = int(typein[1])
horsex = int(typein[2])
horsey = int(typein[3])
endx += 2
endy += 2
horsex += 2
horsey += 2
f[2][1] = 1
for i in range(9):
    board[horsex + fx[i]][horsey + fy[i]] = 1
for i in range(2, endx + 1):
    for j in range(2, endy + 1):
        if board[i][j] == 1:
            continue
        f[i][j] = f[i - 1][j] + f[i][j - 1]

print(f[endx][endy])