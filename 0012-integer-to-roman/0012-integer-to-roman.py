class Solution:
    def intToRoman(self, num: int) -> str:
        # understand
        # given an int convert to a roman form

        # match
        # hash map
        

        # plan
        # take length of int
        # iterate over the int and take the num * base
        # if num is 4 or 9 then take next lowest base in front of base

        translate = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"]
        ]
        
        roman_numeral = ""
        for val, sym in translate:
            base = num // val
            if base:
                roman_numeral = roman_numeral + (base * sym)
                num = num % val
        return roman_numeral