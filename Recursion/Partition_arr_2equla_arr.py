class Solution(object):
    def checkEqualPartitions(self, nums, target):

        total = 1

        for num in nums:
            total *= num

        if total != target * target:
            return False


        def solve(index, product):

            if product == target:
                return True
            if index >= len(nums):
                return False

       
            if product > target:
                return False

            take = solve(index + 1, product * nums[index])

            
            not_take = solve(index + 1, product)

            return take or not_take


        return solve(0, 1)