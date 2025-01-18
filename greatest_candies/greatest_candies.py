"""
Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where 
each candies[i] represents the number of candies the ith kid has, and an 
integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after 
giving the ith kid all the extraCandies, they will have the greatest number of 
candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2, 3, 5, 1, 3], extraCandies = 3
Output: [true, true, true, false, true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the 
  kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:
Input: candies = [4, 2, 1, 1, 2], extraCandies = 1
Output: [true, false, false, false, false]
Explanation: There is only 1 extra candy. Kid 1 will always have the greatest 
number of candies, even if a different kid is given the extra candy.

Example 3:
Input: candies = [12, 1, 12], extraCandies = 10
Output: [true, false, true]
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        boolean_array = []
        true, false = True, False
        for candy in candies:
            if candy + extraCandies >= max_candy:
                boolean_array.append(true)
            else:
                boolean_array.append(false)
        return boolean_array


candies = [2, 3, 5, 1, 3]
extraCandies = 3

sol = Solution()
result = sol.kidsWithCandies(candies, extraCandies)
print(result)

"""
EXPLANATION:

1. **Find the Maximum Candies**:
   - First, we find the maximum number of candies that any kid currently has. 
     This helps us determine the target number of candies each kid needs to 
     reach or exceed to be considered as having the greatest number of candies.

2. **Create a Result List**:
   - We create an empty list called `boolean_array` to store the results for 
     each kid.

3. **Check Each Kid**:
   - For each kid, we check if giving them all the extra candies would make 
     their total candies greater than or equal to the maximum number of candies 
     found in step 1.
   - If yes, we add `True` to the result list, indicating that this kid can have 
     the greatest number of candies.
   - If no, we add `False` to the result list, indicating that this kid cannot 
     have the greatest number of candies even with the extra candies.

4. **Return the Result**:
   - Finally, we return the result list, which contains `True` or `False` for 
     each kid based on whether they can have the greatest number of candies or 
     not.
"""
