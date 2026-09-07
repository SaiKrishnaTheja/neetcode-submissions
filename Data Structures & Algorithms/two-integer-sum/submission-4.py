class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums={}
        for index,num in enumerate(nums):
            dict_nums[num]=index
        print(dict_nums)
        for index,num in enumerate(nums):
            if target-num in dict_nums and index!=dict_nums[target-num]:
                return [index,dict_nums[target-num]]