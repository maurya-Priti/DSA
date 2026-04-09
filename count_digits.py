n=1234567
count=0
while(n!=0):
    n=abs(n)
    #add edge cases, eg. when n=0, digit count is 1
    n=n//10
    count+=1
print(count)
