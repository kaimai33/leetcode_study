class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        curr = word[0]
        cnt = 1
        for i in range(1, len(word)):
            if word[i] == curr:
                if cnt == 9:
                    ans += str(cnt) + str(curr)
                    cnt = 1
                else:
                    cnt += 1
            elif word[i] != curr:
                ans += str(cnt) + str(curr)
                curr = word[i]
                cnt = 1
        ans += str(cnt) + str(curr)
        return ans
