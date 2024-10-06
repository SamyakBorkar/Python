class Solution(object):
    def plusOne(self, digits):
         if digits[-1]==9:
            return self.Last_Digit_9(digits)
         else :
            digits[len(digits)-1]= digits[len(digits)-1]+1
            return digits

    def Last_Digit_9(self, list):
         if len(list)==1 and list[0]==9:
            return [1, 0]
         if list[-1] == 9:
            list[-1] = 0
            list[:-1] = self.plusOne(list[:-1])
            return list

sl=Solution()
l=[1,2,9]
print(sl.plusOne(l))