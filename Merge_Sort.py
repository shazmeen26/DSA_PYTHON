
def merge(left,right):
    new = []
    i,j = 0,0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i=i+1
        else:
            new.append(right[j])
            j=j+1
            
    new.extend(left[i:])
    new.extend(right[j:])
    return new

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    return merge(l_half,r_half)


arr = [10,78,23,1,90,101,67,56,34,89,93,87]
sorted_array = merge_sort(arr) 
print("Sorted Array",sorted_array)
        
