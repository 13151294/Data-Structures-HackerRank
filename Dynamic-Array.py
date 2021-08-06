arr = []
ans = 0
n, q = (int(i) for i in input().split())
for i in range(n):
    arr.append([])
for i in range(q):
    cmd, x, y = (int(i) for i in input().split())
    index = (x^ans)%n
    if (cmd == 1):
        arr[index].append(y)
    elif (cmd == 2):
        ans = arr[index][y%len(arr[index])]
        print(ans)
