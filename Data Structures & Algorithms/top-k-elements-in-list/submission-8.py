class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        seen = set()
        count = 0
        for num in nums:
            if freq.get(num) == None:
                count += 1
                freq[num] = 1
                if count <= k:
                    seen.add(num)
                continue
            freq[num] += 1
            if num in seen:
                continue
            for index in seen:
                if freq.get(index) < freq.get(num): 
                    seen.remove(index)
                    seen.add(num)
                    break
        return list(seen)