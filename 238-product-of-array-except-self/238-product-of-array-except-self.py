class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        product = 1
        flag = False
        count = 0
        for item in nums:
            if item==0:
                flag=True
                count+=1
                
           
            else:
                product*=item
        
        if count>1:
            product=0
        for i in range(len(nums)):
            num = nums[i]
            if num==0:
                arr.append(product)
            elif flag==True:
                arr.append(0)
            else:
                val = product//num
                arr.append(val)
        nums.sort()
        if nums[-1]==0:
            return nums
        return arr