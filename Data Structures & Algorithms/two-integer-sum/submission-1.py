class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fmap = {}
        for index, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in fmap:
                index2 = fmap[num2]
                return [index, index2] if index2 > index else [index2, index]
            fmap[num1] = index