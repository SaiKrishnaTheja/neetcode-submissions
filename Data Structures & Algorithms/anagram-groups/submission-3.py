from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord("a")]+=1
            data[tuple(count)].append(word)
        print(list(data.values()))
        return list(data.values())

        


        