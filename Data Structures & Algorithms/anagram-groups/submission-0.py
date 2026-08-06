class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = dict()

        for string in strs:
            count = [0]*26
            for c in string:
                count[ord(c)-ord("a")]+=1
            
            if tuple(count) in output:
                output[tuple(count)].append(string)
            else:
                output[tuple(count)]=[string]
        print(output)
        return output.values()