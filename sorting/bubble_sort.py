def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([100,20,30,15,3,2,15,26]))


def optimized_bubble_sort(arr):
    for i in range(0,len(arr)-1):
        isSwapped=False
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                isSwapped=True
        if not isSwapped:
            break
    return arr
print(bubble_sort([100,20,30,15,3,2,15,26]))