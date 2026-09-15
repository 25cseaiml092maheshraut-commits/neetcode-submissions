class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rows = len(nums)
        for i in range(rows - 1):
            for j in range(i + 1, rows):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
        