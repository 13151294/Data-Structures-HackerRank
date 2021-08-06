n, q = (int(i) for i in input().split())
arr = input().split()
arr = arr[q:]+arr[:q]
print(' '.join(arr))
