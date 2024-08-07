class Solution:
    def numberToWords(self, num: int) -> str:
        # I just read the answer lol, here is my typing it all up from memory
        if num == 0:
            return "Zero"

        belowTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def helper(num):
            if num < 20:
                string = belowTwenty[num]
            elif num < 100:
                # belowTwenty will only access ones digit from 0-9 in this case
                string = tens[num//10] + " " + belowTwenty[num%10]
            elif num < 1000:
                string = helper(num//100) + " Hundred " + helper(num%100)
            elif num < 1000000:
                string = helper(num//1000) + " Thousand " + helper(num%1000)
            elif num < 1000000000:
                string = helper(num//1000000) + " Million " + helper(num%1000000)
            else:
                string = helper(num // 1000000000) + " Billion " + helper(num%1000000000)
            
            return string.strip()
        
        return helper(num)
        
        