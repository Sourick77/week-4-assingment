class Solution:
    def josephus(self, n, k):
        result = 0  # Base case: position 0 when there's only 1 person (0-indexed)
        for i in range(2, n + 1):
            result = (result + k) % i
        return result + 1  # Convert to 1-based index

