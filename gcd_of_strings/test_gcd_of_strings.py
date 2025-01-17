import pytest
from gcd_of_strings import Solution

@pytest.fixture
def solution():
    return Solution()

def test_gcd_of_strings_example1(solution):
    assert solution.gcdOfStrings("ABCABC", "ABC") == "ABC"

def test_gcd_of_strings_example2(solution):
    assert solution.gcdOfStrings("ABABAB", "ABAB") == "AB"

def test_gcd_of_strings_example3(solution):
    assert solution.gcdOfStrings("LEET", "CODE") == ""

if __name__ == "__main__":
    pytest.main()