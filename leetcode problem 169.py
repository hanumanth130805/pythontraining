
def majorityElement(nums):
        c=0
        candiate=0
        for num in nums:
            if c==0:
                candiate=num
                c+=1
            elif candiate==num:
                    c+=1
            else:
                 c-=1
        return candiate
print(majorityElement([1,2,2,1,2,2,1]))