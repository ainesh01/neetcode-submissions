from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        for c_s in s:
            map_s[c_s] = map_s.get(c_s,0)+1
        
        map_t = {}
        for c_t in t:
            map_t[c_t] = map_t.get(c_t,0)+1
        
        return map_t == map_s

        