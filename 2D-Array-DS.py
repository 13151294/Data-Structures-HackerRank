arr = []
sumarr = []
height = 6
width = 6
for i in range(height):
    arr.append([int(i) for i in input().split()])
for i in range(height-2):
    for j in range(width-2):
        first = arr[0+i][0+j]+arr[0+i][1+j]+arr[0+i][2+j]
        mid = arr[1+i][1+j]
        last = arr[2+i][0+j]+arr[2+i][1+j]+arr[2+i][2+j]
        sumarr.append(first+mid+last)
print(max(sumarr))
