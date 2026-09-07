from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict=defaultdict(list)
        for word in strs:
            data = [0]*26
            for char in word:
                data[ord(char)-ord("a")]+=1
            group_dict[tuple(data)].append(word)
        return list(group_dict.values())

        


        