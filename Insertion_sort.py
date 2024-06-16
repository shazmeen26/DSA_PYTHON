def insertion_sort(arr1):
    n = len(arr1)
    for i in range(1,n):
        key = arr1[i]
        j = i-1
        while j>=0 and key < arr1[j]:
            arr1[j+1]=arr1[j]
            j= j-1
        arr1[j+1] = key 


arr1 = [10,78,23,1,90,101,67,56,34,89,93,87]
insertion_sort(arr1)
print("Sorted Array is:",arr1)
