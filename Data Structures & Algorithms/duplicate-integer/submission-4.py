class Solution:
    # Brute force solution
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False
    # Sorting first solution
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     if len(nums) <= 1: 
    #         return False
    #     for i in range(len(nums)):
    #             if nums[i] == nums[i - 1]:
    #                 return True
    #     return False
    # Hash set solution
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
        