class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)): 
            if sdict.get(s[i]) == None:
                sdict[s[i]] = 0
            else:
                current = sdict.get(s[i]) + 1
                sdict[s[i]] = current
            if tdict.get(t[i]) == None:
                tdict[t[i]] = 0
            else:
                current = tdict.get(t[i]) + 1
                tdict[t[i]] = current
        for key in sdict.keys():
            print(sdict.get(key))
            print(tdict.get(key))
            if sdict.get(key) != tdict.get(key):
                return False
        return True