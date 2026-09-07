class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        dict_1={}
        for i in s:
            dict_1[i]=dict_1.get(i,0)+1
        print(dict_1)
        dict_2={}
        for i in t:
            dict_2[i]=dict_2.get(i,0)+1
        print(dict_2)
        
        for i,j in dict_1.items():
            if dict_1[i]!=dict_2.get(i,0):
                return False
        return True
        

       