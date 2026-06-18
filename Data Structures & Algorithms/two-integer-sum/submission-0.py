class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = defaultdict(int)
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], idx]
            numMap[num] = idx
        return []