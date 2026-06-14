class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        re = []

        x = 0
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if j == x:
                    continue
                num *= nums[j]
                j += 1

            re.append(num)
            x += 1
            i += 1
        
        return re
        