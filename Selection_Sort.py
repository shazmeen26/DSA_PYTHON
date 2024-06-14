def selection_sort(arr1):

    n = len(arr1)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr1[j]<arr1[min]:
                min = j
                (arr1[i],arr1[min])=(arr1[min],arr1[i])



arr1 = [10,78,23,1,90,101,67,56,34,89,93,87]
selection_sort(arr1)
print("Sorted Array: ",arr1)
