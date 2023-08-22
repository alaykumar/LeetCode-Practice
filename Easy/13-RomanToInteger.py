class Solution:
    def romanToInt(self, s: str) -> int:

        # Reference dictionary for Roman characters to integers
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

        # final answer variable
        ans = 0

        # for loop to iterate through each character in the Roman numeral string
        for c in range(len(s)):

            # if the count is less than the length of the Roman numeral string and if the current Roman character is less than its next character then subtract its value from the answer
            if c < len(s) - 1 and d[s[c]] < d[s[c+1]]:
                ans -= d[s[c]]

            # Otherwise add the value into the answer
            else:
                ans += d[s[c]]

        # return answer
        return ans
