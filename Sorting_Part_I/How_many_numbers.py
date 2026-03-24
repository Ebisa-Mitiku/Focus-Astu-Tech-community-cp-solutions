class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(len(nums)):
            d=0
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    d+=1
            k.append(d)
        return(k)
