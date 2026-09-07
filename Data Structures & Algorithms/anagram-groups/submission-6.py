from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict={}
        for word in strs:
            data = [0]*26
            for char in word.lower():
                data[ord(char)-ord("a")]+=1
            if tuple(data) not in group_dict:
                group_dict[tuple(data)]=[]
            
            group_dict[tuple(data)].append(word)
        return list(group_dict.values())

        


        