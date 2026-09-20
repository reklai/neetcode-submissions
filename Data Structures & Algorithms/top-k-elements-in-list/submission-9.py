class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = []
        res = []
        for _ in range(0, len(nums) + 1):
            bucket.append([])
        for num in nums:
            if freq.get(num) == None:
                freq[num] = 1
                continue
            freq[num] += 1
        for num, count in freq.items():
            bucket[count].append(num)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res