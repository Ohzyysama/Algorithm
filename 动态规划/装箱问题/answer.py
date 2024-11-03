V = int(input())
n = int(input())
items = []
for i in range(n):
    v = int(input())
    items.append(v)
dp = [[0] * (V+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, V+1):
        if items[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1]] + items[i-1])
v_left = V - dp[n][V]
print(f"{v_left}")