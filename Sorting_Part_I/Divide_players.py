class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        total=skill[0]+skill[n-1]
        l=0
        r=n-1
        chem=0
        while(l<r):
            if(skill[l]+skill[r]==total):
                chem+=(skill[l]*skill[r])
                l+=1
                r-=1
            else:
                return -1
        return chem
