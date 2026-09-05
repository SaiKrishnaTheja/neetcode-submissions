class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for char in s:
            freq[char]=freq.get(char,1)+1
        freq_2={}
        for char in t:
            freq_2[char]=freq_2.get(char,1)+1
        return freq==freq_2
        