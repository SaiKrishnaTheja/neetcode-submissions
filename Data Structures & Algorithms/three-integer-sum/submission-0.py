from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_map = defaultdict()
        for i,j in enumerate(nums):
            hash_map[j]=i
        result= set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if -(nums[i]+nums[j]) in hash_map:
                    k = hash_map[-(nums[i]+nums[j])]
                    if i!=k and j!=k:
                        result.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return list(list(r) for r in result)


        
        