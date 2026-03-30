class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

    # Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

    # Sort by frequency in descending order
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Take first k elements
        result = [item[0] for item in sorted_items[:k]]

        return result
        