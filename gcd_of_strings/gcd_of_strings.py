"""
Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ...
+ t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides
both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""
from math import gcd

class Solution:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]

str1 = "ABCABC"
str2 = "ABC"
solution = Solution()
print(solution.gcdOfStrings(str1, str2))

"""
EXPLANATION:

1. Check concatenation: The code first checks if the concatenation of str1 and 
   str2 in both possible orders (str1 + str2 and str2 + str1) is the same. If 
   not, it returns an empty string because there is no common divisor.
2. Find GCD of lengths: The code uses the math.gcd function to find the greatest
   common divisor of the lengths of str1 and str2.
3. Return the GCD string: The GCD string is the prefix of str1 with the length 
   equal to the GCD of the lengths of str1 and str2.
"""

"""
len(str1) and len(str2): These functions calculate the lengths of the strings 
str1 and str2. For example, if str1 is "ABCABC" and str2 is "ABC", then len(str1) 
is 6 and len(str2) is 3.

math.gcd(a, b): This function from the math module calculates the greatest 
common divisor (GCD) of two numbers a and b. The GCD is the largest number that 
can evenly divide both a and b. For example, the GCD of 6 and 3 is 3 because 3 
is the largest number that can divide both 6 and 3 without leaving a remainder.

Putting it together: math.gcd(len(str1), len(str2)) calculates the GCD of the 
lengths of str1 and str2. This gives us the length of the longest string that 
can be repeated to form both str1 and str2.
"""