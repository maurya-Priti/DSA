#merge sort
nums=[100,0,2,15,11,3,9,7]


def merge_sort(arr):
  if len(arr)<=1:
    return arr
  
  mid = len(arr)//2

  left = merge_sort(arr[0:mid])
  right = merge_sort(arr[mid:])

  return merge(left,right)

def merge(left,right):

  result=[]
  i=0;j=0
  while(i<len(left) and j<len(right)):
    
    if left[i]>right[j]:
      result.append(right[j])
      j+=1
    else:
      result.append(left[i])
      i+=1
  result.extend(right[j:])
  result.extend(left[i:])
  return result

print(merge_sort(nums))

