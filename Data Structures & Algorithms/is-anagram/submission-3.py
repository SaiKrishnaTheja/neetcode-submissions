class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict_1 = {}
        for i in s:
            if i not in freq_dict_1:
                freq_dict_1[i]=1
            else:
                freq_dict_1[i]+=1
        freq_dict_2 = {}
        for i in t:
            if i not in freq_dict_2:
                freq_dict_2[i]=1
            else:
                freq_dict_2[i]+=1
        return freq_dict_1==freq_dict_2