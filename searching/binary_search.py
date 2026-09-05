#linear search
nums=[1,2,3,4,5,6,7,8,9]
target=9
l=0
r=len(nums)-1

while(l<=r):
  mid=(l+r)//2
  if target>nums[mid]:
    l=l+1
  elif target < nums[mid]:
    r=r-1
  else:
    print(mid)
    break
else:
  print(-1)
