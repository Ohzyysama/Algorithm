T, M = map(int, input().split())
grass = []
for i in range(M):
    t, v = map(int, input().split())
    grass.append((t, v))

dp = [[0] * (T + 1) for i in range(M+1)]
for i in range(1, M+1):
    for j in range(1, T+1):
        if grass[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-grass[i-1][0]] + grass[i-1][1])
    
print(dp[M][T])