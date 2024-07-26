class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        v1 = alpha[coordinates[0]]
        v2 = int(coordinates[1])
        return False if (v1 + v2) % 2 == 0 else True