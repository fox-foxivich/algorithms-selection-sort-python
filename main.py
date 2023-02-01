# Big O(n^2)
def findSmallestItemIndex(arr):
    smallest_index = 0
    smallest_item = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest_item:
            smallest_item = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_item_index = findSmallestItemIndex(arr)
        newArr.append(arr.pop(smallest_item_index))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))