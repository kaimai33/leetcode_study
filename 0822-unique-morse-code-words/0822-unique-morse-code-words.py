class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        concatenations = set()
        for word in words:
            string = ""
            for c in word:
                string += morse[ord(c) - ord('a')]
            concatenations.add(string)
        return len(concatenations)