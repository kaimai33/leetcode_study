class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set()
        for c in allowed:
            allowed_set.add(c)
        ans = 0
        for word in words:  
            checked_vals = 0
            for c in word:
                if c not in allowed_set:
                    continue
                else:
                    checked_vals += 1
                if checked_vals == len(word):        
                    ans += 1
        return ans