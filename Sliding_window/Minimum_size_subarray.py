class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ml=float('inf')
        cur_s=0
        for i in range(len(nums)):
            cur_s=cur_s+nums[i]
            while(cur_s>=target):
                ml=min(ml,i+1-left)
                cur_s=cur_s-nums[left]
                left=left+1
        if(ml==float('inf')):
            return(0)
        return(ml)
