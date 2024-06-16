def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i = i + 1
        while i <= j and arr[j] >= p:
            j = j - 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [10, 78, 23, 1, 90, 101, 67, 56, 34, 89, 93, 87]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted Array is:", arr)
