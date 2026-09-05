class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        data ={}
        for i in range(len(nums)):
            data[nums[i]]=i
        print(data)
        for j in range(len(nums)):
            if target-nums[j] in data and j!=data[target-nums[j]]:
                return [j,data[target-nums[j]]]
