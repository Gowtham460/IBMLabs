num=int(input("Enter the num:"))
fact=1
if num<0:
    print("Sorry,factorial doesn't exist for negative number")
elif num==0:
    print("The factorial for 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorail of",num,"is",fact)