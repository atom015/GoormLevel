n = int(input())
arr = list(map(int,input().split()))
find_value = int(input())
if find_value in arr:
	print(arr.index(find_value)+1)
else:
	print("X")
