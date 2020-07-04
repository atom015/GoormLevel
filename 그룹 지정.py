def Get(x):
	if p[x] == x:
		return x
	p[x] = Get(p[x])
	return p[x]


def union(a, b):
	a = Get(a)
	b = Get(b)
	if a < b:
		p[b] = a
	elif a > b:
		p[a] = b


N, M = map(int, input().split())
p = [i for i in range(N+1)]
Set = set()
for i in range(M):
	a, b = map(int, input().split())
	union(a, b)
for i in range(1, N+1):
	Set.add(Get(i))
print(len(Set))
