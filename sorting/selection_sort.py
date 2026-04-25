def selection_sort(arr):

   for i in range(0,len(arr)):
       min=i

       for j in range(i, len(arr)):
           if arr[j]<arr[min]:
               min=j

       arr[i],arr[min]=arr[min],arr[i]
   return arr
print(selection_sort([100,20,30,15,3,2,15,26]))



#optimized:
def opt_selection_sort(arr):

   for i in range(0,len(arr)):
       min=i

       for j in range(i, len(arr)):
           if arr[j]<arr[min]:
               min=j

       if (min!=i):
           arr[i],arr[min]=arr[min],arr[i]

   return arr
print(opt_selection_sort([100,20,30,15,3,2,15,26]))

def alt_selection_sort(arr):

   for i in range(0,len(arr)):
       min=i

       for j in range(i+1, len(arr)):
           if arr[j]<arr[min]:
               min=j

       arr[i],arr[min]=arr[min],arr[i]
   return arr
print(alt_selection_sort([100,20,30,15,3,2,15,26]))
