def findlowindex(arr):
    lis_index = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < lis_index:
            lis_index = arr[i]
            index = i
            
    return index

def sort(arr, arr2 = []):
    for i in range(len(arr)):
        new = findlowindex(arr)
        arr2.append(arr.pop(new))
    return arr2
print(sort([2, 3, 0, 56]))
        
