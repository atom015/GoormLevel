n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
visited = [[False for i in range(n)] for i in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = [[0,0,1]]
visited[0][0] = True
while len(q) != 0:
	x,y,cost = q.pop(0)
	if x == n-1 and y == n-1:
		break
	for i in range(4):
		nx = x+dx[i]
		ny = y+dy[i]
		if 0 <= nx < n and 0 <= ny < n:
			if arr[nx][ny] == 1 and visited[nx][ny] == False:
				q.append([nx,ny,cost+1])
				visited[nx][ny] = True
print(cost)
