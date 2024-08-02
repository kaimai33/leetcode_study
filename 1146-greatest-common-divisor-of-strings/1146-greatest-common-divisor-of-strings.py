class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        # we reduce both strings until we reach a shared similar component
        while len(str2) > 0:
            if str1 == str2:
                return str1
            if str1.startswith(str2):
                str1 = str1[len(str2):]
            elif str2.startswith(str1):
                str2 = str2[len(str1):]
            else:
                return ""
        
        return str1