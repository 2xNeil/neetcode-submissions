class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fmap = {}
        for index, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in fmap:
                index2 = fmap[num2]
                return [min([index, index2]), max([index, index2])]
            fmap[num1] = index