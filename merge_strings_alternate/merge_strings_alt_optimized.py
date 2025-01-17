import time


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        len1, len2 = len(word1), len(word2)
        for i in range(min(len1, len2)):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.append(word1[i + 1 :])
        merged.append(word2[i + 1 :])
        return "".join(merged)


# word1 = "abc"
# word2 = "pqr"

word1 = "ab"
word2 = "pqrs"

# word1 = "abcd"
# word2 = "pq"

sol = Solution()

result = sol.mergeAlternately(word1, word2)


print(f"Result: {result}")
