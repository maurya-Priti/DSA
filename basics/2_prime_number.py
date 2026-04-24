class Solution:
    def check_prime(self,n):
        for i in range(2,n-1):
            if n%i==0:
                return False
        return True

test=Solution()
print(test.check_prime(7))