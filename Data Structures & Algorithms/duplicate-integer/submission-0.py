class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        currentDict = {}
        for i in range(0, len(nums)):
            if currentDict.get(nums[i]) == None:
                currentDict[nums[i]] = 0
            else:
                return True
        return False
