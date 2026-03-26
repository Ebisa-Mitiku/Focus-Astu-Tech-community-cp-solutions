class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat=0
        seen=set()
        r=len(people)-1
        for i in range(len(people)//2):
            while(i<r):
                if(people[i]+people[r]>limit):
                    r-=1
                else:
                    seen.add(i)
                    seen.add(r)
                    boat+=1
                    r-=1
                    break
        if(len(seen)<len(people)):
            boat+=(len(people)-len(seen))          
        return boat

           




    

        
