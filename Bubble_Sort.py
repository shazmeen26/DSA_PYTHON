def bubble_sort(arr1):
    n=len(arr1)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr1[j]>arr1[j+1]:
                swapped = True
                arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                
        if not swapped:
            return



arr1 = [10,78,23,1,90,101,67,56,34,89,93,87]
bubble_sort(arr1)
print("Sorted Array is:")
for i in range(len(arr1)):
    print("% d" % arr1[i], end=" ")
