class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        values = list(map(lambda char: roman_numerals[char], s))
        
        total = 0
        prev_value = 0
        
        for value in reversed(values):
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
            
        return total

solution = Solution()
print(solution.romanToInt("MCMXCIV"))
