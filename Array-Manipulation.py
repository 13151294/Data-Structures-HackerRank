def method(n,q):
    arr = [0]*n
    for i in q:
        arr[i[0]-1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    maxval = 0
    now = 0
    for i in arr:
        now += i
        if now > maxval:
            maxval = now
    return maxval

n, q = (int(i) for i in input().split())
q = [list(map(int, input().split())) for i in range(q)]
print(method(n,q))
