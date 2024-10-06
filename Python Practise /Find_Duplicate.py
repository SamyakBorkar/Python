from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         nums.sort()
         for i in range(1, len(nums)):
            if nums[i-1]==nums[i]:
                return True
         return False

        




sol= Solution()
list=[1,2,3,1]
print(sol.containsDuplicate(list))