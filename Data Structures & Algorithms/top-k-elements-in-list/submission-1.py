from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in range(len(nums)):
            d[nums[i]] += 1
        
        top_k = []

        sorted_desc = sorted(d, key=lambda x: d[x], reverse=True)

        for i in range(k):
            top_k.append(sorted_desc[i])
        
        return top_k

        