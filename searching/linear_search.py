def linear_search(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i
    else:
        return -1

arr=[10,2,6,18,100,20]
print(linear_search(arr,6))


