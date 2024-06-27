def findMin(arr):
    min = arr[0]
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_idx = i
    return min_idx

def selectionSort(arr):
    newArr = []
    for _ in range(len(arr)):
        min = findMin(arr)
        newArr.append(arr.pop(min))
    return newArr

print(selectionSort([5, 3, 2, 10, 999, 0, 21, 25]))