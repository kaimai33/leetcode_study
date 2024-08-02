class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Thought process:
        1. reverse senate to turn it into a stack
        2. we parse through the stack. we will always ban people from the other team.
        3. keep track of remaining counts of each party. when we reach 0, we have a winner.

        """

        radiant = deque()
        dire = deque()

        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        
        if len(radiant) > len(dire):
            return "Radiant"
        else:
            return "Dire"