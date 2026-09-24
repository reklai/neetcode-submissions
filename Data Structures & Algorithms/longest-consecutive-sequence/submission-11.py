class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0
        for i in range(0, len(nums)):
            seen.add(nums[i])
        for num in seen:
            if num - 1 not in seen:
                streak = 1
                while (num + streak) in seen:
                    streak += 1
                    if streak >= longest:
                        longest = streak
        if len(nums) == 0:
            return 0
        if longest == 0:
            return 1
        return longest 