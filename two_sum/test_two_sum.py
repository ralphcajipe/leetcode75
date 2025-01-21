import pytest
from two_sum import Solution

@pytest.fixture

def solution():
    return Solution()

def test_two_sum_example1(solution):
    assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
    
def test_two_sum_example2(solution):
    assert solution.two_sum([3, 2, 4], 6) == [1, 2]
    
def test_two_sum_example3(solution):
    assert solution.two_sum([3, 3], 6) == [0, 1]
    
if __name__ == "__main__":
    pytest.main()
