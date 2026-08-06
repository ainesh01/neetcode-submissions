class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Count = {}
        for c in s1:
            s1Count[c] = s1Count.get(c,0) +1
        
        for i in range(len(s2)-len(s1)+1):
            s2Count = {}
            for j in range(i, i+len(s1)):
                s2Count[s2[j]] = s2Count.get(s2[j],0) +1
            print(s1Count)
            print(s2Count)
            if s1Count == s2Count:
                return True
        return False