class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        cout=nums.count(0)
        for i in nums:
            if(i!=0):
                product=product*i
        if(cout>1):
            for i in range(len(nums)):
                nums[i]=0
            return(nums)
        elif(cout==1):
            x=nums.index(0)
            nums[x]=product
            for i in range(len(nums)):
                if(i!=x):
                    nums[i]=0
            return(nums)
        else:
            for i in range(len(nums)):
                nums[i]=product//nums[i]
            return(nums)
    
        
            
            

        
