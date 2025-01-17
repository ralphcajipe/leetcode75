"""
Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range(min(len(word1), len(word2))):
            merged += word1[i] + word2[i]
        return merged + word1[i + 1:] + word2[i + 1:]

word1 = "abc"
word2 = "pqr"

# word1 = "ab"
# word2 = "pqrs"

# word1 = "abcd"
# word2 = "pq"

sol = Solution()
result = sol.mergeAlternately(word1, word2)
print(result)

"""
EXPLANATION:

The provided code defines a class Solution with a method mergeAlternately that 
takes two strings, word1 and word2, as input and merges them alternately. The 
method initializes an empty string merged to store the result. It then iterates 
over the indices of the shorter string (determined by min(len(word1), len(word2))) 
and appends characters from both strings alternately to merged. After the loop, 
it appends the remaining characters from the longer string to merged by slicing 
from the current index i+1 to the end of each string. This ensures that all 
characters from both strings are included in the final merged string.

The code also includes a test case where word1 is "ab" and word2 is "pqrs". An 
instance of the Solution class is created, and the mergeAlternately method is 
called with word1 and word2 as arguments. The result is printed to the console. 
In this case, the output will be "apbqrs" because the characters from word1 and 
word2 are alternately merged until word1 is exhausted, and then the remaining 
characters from word2 are appended.

Overall, the code demonstrates a straightforward approach to merging two strings 
alternately, handling cases where the strings are of different lengths by 
appending the remaining characters from the longer string.

Merging two words alternately involves taking characters from each word one by 
one and combining them into a new string. Here's a step-by-step explanation of 
how the provided code accomplishes this:

1. Initialization:
- Two input strings, word1 and word2, are defined.
- An empty string merged is initialized to store the result.

2. Iterating through the strings:
- The code uses a for loop to iterate over the indices of the shorter string. 
  This is determined by min(len(word1), len(word2)).
- For each index i, the code appends the i-th character from both word1 and 
  word2 to the merged string.

3. Appending remaining characters:
- After the loop, there may be remaining characters in the longer string (if the 
  strings are of different lengths).
- The code appends the remaining characters from both word1 and word2 starting 
  from the index i+1 to the end of each string.

4. Returning the result:
- The final merged string is returned.
"""