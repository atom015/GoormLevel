N = int(input())
dp = []
for i in range(N*2-1):
	dp.append(list(map(int,input().split())))
for i in range(1,N):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j]+dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i][j]+dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j]+max(dp[i-1][j],dp[i-1][j-1])
for i in range(N,N*2-1):
    for j in range(len(dp[i])):
        dp[i][j] = dp[i][j]+max(dp[i-1][j],dp[i-1][j+1])
print(dp[N*2-2][0])
