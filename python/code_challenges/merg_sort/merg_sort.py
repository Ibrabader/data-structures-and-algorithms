def mergSort(arr):
    n=len(arr)
    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right= arr[mid:n]
        mergSort(left)
        mergSort(right)
        return merge(left, right, arr)

def merge(left, right, arr):
        i=0
        y=0
        z=0

        while i < len(left) and y < len(right):
            if left[i] < right[y]:
                arr[z] = left[i]
                i += 1
            else:
                arr[z] = right[y]
                y += 1
            z += 1

            
        if i == len(left):
            for item in right[y:]:
                arr[z] = item
                z += 1
        else:
            for item in left[i:]:
                arr[z] = item
                z += 1
        return (arr)



print(mergSort([8,4,23,42,16,15]))

