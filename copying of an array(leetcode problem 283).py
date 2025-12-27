def movzeroes(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]==0:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=x+y
    print(z)
nums=[0,1,0,3,12]
movzeroes(nums)