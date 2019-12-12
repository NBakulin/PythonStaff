def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr):
    low = 0
    high = len(arr) - 1
    pi = partition(arr, low, high)
    quickSortPartition(arr, low, pi - 1)
    quickSortPartition(arr, pi + 1, high)


def quickSortPartition(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSortPartition(arr, low, pi - 1)
        quickSortPartition(arr, pi + 1, high)


list = [2, 3, 6, 8, 1, 9, 4, 5, 7]
quickSort(list)

print(list)
