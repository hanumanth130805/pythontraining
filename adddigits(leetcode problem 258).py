def adddigits(num):
    while num>=10:
        sumi=0
        while num>0:
            rem=num%10
            sumi+=rem
            num=num //10
        num=sumi
    return num
num=134
print(adddigits(num))