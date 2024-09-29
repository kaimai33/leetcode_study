class Solution:
    def kthCharacter(self, k: int) -> str:
        string = "a"
        while len(string) < k:
            new_part = ""
            for c in string:
                if c == 'z':
                    new_part += 'a'
                else:
                    new_part += chr(ord(c) + 1)
            string += new_part
        return string[k-1]