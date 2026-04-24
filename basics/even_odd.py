class Solution:
    def even_odd(self, nums):
        if nums%2==0:
            return "Even"
        else:
            return "Odd"

test=Solution()
print(test.even_odd(15))

