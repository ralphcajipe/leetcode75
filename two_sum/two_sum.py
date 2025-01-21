"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def two_sum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return "No two sum solution found"


nums = [3, 3]
target = 6

sol = Solution()
result = sol.two_sum(nums, target)
print(result)  # Output: [0, 1]

"""
EXPLANATION:

1. **Dictionary for Seen Numbers**:
   - We use a dictionary `seen` to keep track of the indices of the numbers 
     we've encountered so far.

2. **Iterate Through the List with Indices**:
   - We use `enumerate` to get both the index and the number.

3. **Calculate Complement**:
   - For each number, we calculate its complement with respect to the target.

4. **Check for Complement**:
   - We check if the complement is already in the dictionary.
   - If it is, we return the indices `[seen[complement], i]`.
   - If it isn't, we add the current number and its index to the dictionary.

5. **No Solution Found**:
   - If the loop completes without finding a pair, we return "No two sum 
     solution found".

This approach ensures that we efficiently find the pair of numbers that add up 
to the target or indicate that no such pair exists. The use of a dictionary 
allows us to achieve this in O(n) time complexity and correctly handles cases 
with duplicate numbers.
"""
