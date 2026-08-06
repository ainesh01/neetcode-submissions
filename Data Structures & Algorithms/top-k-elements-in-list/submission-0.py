class Solution:

    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def sortFunc(self, freq: List[int]) -> int: 
            return freq[1]
        numFreq = {}
        for num in nums:
            numFreq[num] = 1+numFreq.get(num, 0)

        freqList = [[num, numFreq[num]] for num in numFreq]

        print(freqList)
        freqList.sort(key=lambda x:x[1], reverse=True)
        print(freqList)
        res = []
        for i in range(k):
            res.append(freqList[i][0])
        
        return res

