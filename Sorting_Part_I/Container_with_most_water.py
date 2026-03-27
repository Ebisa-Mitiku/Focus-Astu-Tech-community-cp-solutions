class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        area=0
        r=len(height)-1
        while(l<r):
            k=min(height[l],height[r])*(r-l)
            area=max(area,k)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
                
        return area
                


       
        
