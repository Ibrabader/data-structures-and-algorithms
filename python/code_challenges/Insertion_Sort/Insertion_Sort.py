arr = [64, 25, 12, 22, 11]
arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    midx = i
    for j in range(i+1, len(arr)):
        if arr[midx] > arr[j]:
            midx = j
    arr[i], arr[midx] = arr[midx], arr[i]
print (arr)
