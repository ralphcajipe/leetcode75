import pytest
from merge_strings_alternate import Solution


@pytest.fixture
def solution():
    """Instantiate solution object"""
    return Solution()


def test_merge_alternately_example1(solution):
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"


def test_merge_alternately_example2(solution):
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"


def test_merge_alternately_example3(solution):
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"


if __name__ == "__main__":
    pytest.main()
