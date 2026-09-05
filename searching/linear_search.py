def linear_search(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i
    else:
        return -1

arr=[10,2,6,18,100,20]
print(linear_search(arr,6))


#linear search
#nums=[1,2,3,4,5,6,7,8,9]
#target=90
#for i,n in enumerate(nums):
#  if n==target:
#    print(i)
#    break
#else:
#  print(-1)

