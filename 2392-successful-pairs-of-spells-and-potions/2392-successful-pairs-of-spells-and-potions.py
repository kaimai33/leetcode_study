class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()

        for spell in spells:
            l, r = 0, len(potions)
            while l < r:
                m = (l + r) // 2
                if spell * potions[m] < success:
                    l = m + 1
                else:
                    r = m

            
            pairs.append(len(potions) - l)


        return pairs