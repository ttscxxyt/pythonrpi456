#calculator
a=float(input("enter a number\n"))
b=float(input("enter a number\n"))
c=int(input("enter a number:add-1,sub-2,division-3,multiply-4\n"))
print("the solution is")
if c==1:
    print(a+b)
if c==2:
    print(a-b)
if c==3:
    if b==0:
        print(" infinity i.e. divisor is zero")
    else:
        print(a/b)
if c==4:
    print(a*b)
