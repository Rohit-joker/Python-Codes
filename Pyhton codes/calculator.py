class calculator:
    def sum(a,b):
        print(a+b)

    def sub(a,b):
        print(a-b)

    def mul(a,b):
        print(a*b)

    def div(a,b):
        print(a/b)

    def sqr(a,b):
        print(a**b)

    def remain(a,b):
        print(a%b)

a=int(input("enter the any num 1: "))
b=int(input("enter the any num 2: "))

print("enter which function you want to perform :")
cal=calculator
print("1 for Sum : ")
print("2 for Sub : ")
print("3 for mul : ")
print("4 for div : ")
print("5 for sqr : ")
print("6 for remain : ")

c=int(input("enter the num of function : "))

if c==1:
    cal.sum(a,b)
elif c==2:
    cal.sub(a,b)
elif c==3:
    cal.mul(a,b)
elif c==4:
    cal.div(a,b)
elif c==5:
    cal.sqr(a,b)
elif c==6:
    cal.remain(a,b)
else:
    print("enter valid function number ...")