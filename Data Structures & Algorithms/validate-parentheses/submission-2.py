class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {"(":")",
        "{":"}",
        "[":"]"}
        stack = []
        for i in s:
            if i in map_dict:
                stack.append(i)
            else:
                if not stack:
                    return False
                char = stack.pop()
                if map_dict[char]!=i:
                    return False
        return not stack

        