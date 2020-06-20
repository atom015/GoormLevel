arr = [i if i % 3 == 0 or i % 5 == 0 else 0 for i in range(1001)]
print(sum(arr[0:int(input())+1]))
