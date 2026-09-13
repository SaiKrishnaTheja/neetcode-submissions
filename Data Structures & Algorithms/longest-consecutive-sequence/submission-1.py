class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        max_seq=0
        for num in nums:
            seq=[]
            if num-1 not in sett:
                seq.append(num)
                while num+1 in sett:
                    seq.append(num+1)
                    num+=1
            max_seq=max(len(seq),max_seq)
        return max_seq                



        