import pytest
from greatest_candies import Solution

@pytest.fixture

def solution():
    return Solution()

def test_greatest_candies_1(solution):
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    assert solution.kidsWithCandies(candies, extraCandies) == [True, True, True, False, True]
    
def test_greatest_candies_2(solution):
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    assert solution.kidsWithCandies(candies, extraCandies) == [True, False, False, False, False]
    
def test_greatest_candies_3(solution):
    candies = [12, 1, 12]
    extraCandies = 10
    assert solution.kidsWithCandies(candies, extraCandies) == [True, False, True]

