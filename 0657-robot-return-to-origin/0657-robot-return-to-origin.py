class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hoz = 0
        vert = 0
        for move in moves:
            if move == 'R':
                hoz += 1
            elif move == 'L':
                hoz -= 1
            elif move == 'U':
                vert += 1
            elif move == 'D':
                vert -= 1
        return hoz == 0 and vert == 0