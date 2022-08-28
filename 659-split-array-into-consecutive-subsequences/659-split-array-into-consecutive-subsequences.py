class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sequences = defaultdict(list)
        
        for x in nums:
            smallest_size = 0
            if len(sequences[x-1]) > 0:
                smallest_size = heappop(sequences[x-1])
            heappush(sequences[x], smallest_size + 1)
        
        return all(len(v) == 0 or v[0] >= 3 for v in sequences.values())