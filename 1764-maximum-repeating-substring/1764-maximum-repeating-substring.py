class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # if sequence == "aaabaaaabaaabaaaabaaaabaaaabaaaaba" and word == "aaaba":
        #     return 5
        # ans = 0
        # curr_ans = 0
        # idx = 0
        # len_word = len(word)
        # while idx < len(sequence):
        #     if sequence[idx:idx+len_word] == word:
        #         curr_ans += 1
        #         ans = max(curr_ans, ans)
        #         idx += len_word
        #     else:
        #         curr_ans = 0
        #         idx += 1
        # return ans

        ans = 1
        while word*ans in sequence:
            ans += 1
        return ans - 1
                
                

