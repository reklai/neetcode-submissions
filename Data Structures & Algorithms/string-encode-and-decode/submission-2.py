class Solution:

    def encode(self, strs: List[str]) -> str:
        combine = ""
        for i in range(0, len(strs)):
            if i == 0:
                combine = strs[i] + "\n"
                continue
            combine = combine + strs[i] + "\n"
        return combine
                
    def decode(self, s: str) -> List[str]:
        current = []
        separate = ""
        for i in range(0, len(s)):
            if s[i] == '\n':
                current.append(separate)
                separate = ""
                continue
            separate = separate + s[i]
        return current
