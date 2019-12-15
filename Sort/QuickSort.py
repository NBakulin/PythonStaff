def sort(array, start_index, end_index):
    if start_index < end_index:
        pivot = partition(array, start_index, end_index)
        sort(array, start_index, pivot - 1)
        sort(array, pivot + 1, end_index)


def partition(array, start_index, end_index):
    pivot_value = array[end_index]

    i = start_index - 1

    for j in range(start_index, end_index):
        if pivot_value > array[j]:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end_index] = array[end_index], array[i + 1]
    return i + 1


list = [2, 12, 4, 5, 1, 7, 8, 9, 3, 11, 6, 10]
sort(list, 0, 11)

print(list)
