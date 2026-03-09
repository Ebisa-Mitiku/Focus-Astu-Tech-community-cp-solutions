class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return(0)
        nums=sorted(list(set(nums)))
        count=1
        x=1
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]-1):
                count=count+1
            
            else:
                count=1
            x=max(x,count)  
        return x

        
