class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumList = []
        currentDict = {}
        for i in range(0, len(nums)):
            if i == 0:
                currentDict[nums[i]] = i
                continue
            if currentDict.get(target - nums[i]) == None:
                currentDict[nums[i]] = i
                continue
            else:
                sumList.append(currentDict.get(target - nums[i]))
                sumList.append(i)
                break
        return sumList