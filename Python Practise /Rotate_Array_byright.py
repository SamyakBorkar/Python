from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        temp=[]
        for i in range(len(nums)-k, len(nums)):
            temp.append(nums[i])
        for i in range(len(nums)-k):
            temp.append(nums[i])
        for i in range(len(nums)):
            nums[i]= temp[i]
            
        

sol=Solution()
list=[1,2,3,4,5,6,7]
print(sol.rotate(list, 3))