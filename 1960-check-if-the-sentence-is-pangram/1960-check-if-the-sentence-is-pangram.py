class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(collections.Counter(sentence)) == 26