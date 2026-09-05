class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            print(word)
            del1=str(len(word))
            print(del1+"#"+word)
            new=del1+"#"+word
            encoded.append(new)
        print(encoded)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        x=s
        i=0
        while i <len(x):
            j = i
            while x[j]!="#":
                j+=1
            length = int(x[i:j])
            result.append(x[j+1:j+1+length])
            i=j+1+length

        return result
