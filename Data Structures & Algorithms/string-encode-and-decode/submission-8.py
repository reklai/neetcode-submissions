class Solution:

    def encode(self, strs: List[str]) -> str:
        combine = ""
        for i in range(0, len(strs)):
            if i == 0:
                combine = str(len(strs[i])) + "#" + strs[i]
                continue
            combine = combine + str(len(strs[i])) + "#" + strs[i]
        return combine
                
    def decode(self, s: str) -> List[str]:
        current = []
        start = 0
        num = 0
        for i in range(0, len(s)):
            if s[i] == "#" and start == 0:
                tmp = s[0:i]
                num = int(tmp)
                end = i+1+num
                current.append(s[i+1:end])
                start = end
                continue
            if s[i] == "#" and start != 0:
                if i < start:
                    continue
                tmp = s[start:i]
                num = int(tmp)
                end = i+1+num
                current.append(s[i+1:end])
                start = end
        return current
