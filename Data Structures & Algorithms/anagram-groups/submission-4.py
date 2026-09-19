class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        point = {}
        final = []
        for s in strs:
            count = [0] * 26
            for c in s:
                position = ord(c) - ord('a')
                count[position] += 1
            if point.get(tuple(count)) == None:
                point[tuple(count)] = [s]
            else:
                point.get(tuple(count)).append(s)
        for key in point:
            final.append(point[key])
        return final