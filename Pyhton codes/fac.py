#Factorial num 

n=int(input("enter the last num of factorial : "))

count=1
fact=1

while count<=n:
    print(count)
    fact=fact*count
    count+=1

print("the factorial of ",n,"is :",fact)

#using recursive function

def fac(n):
    if n==0 or n==1:
        print(n)
        return 1
    else:
        print(n)
        return n*fac(n-1)
    
n=int(input("enter the last num of factorial : "))
result=fac(n)
print("the factorial of ",n,"is :",result)

#fibonacci series

a=int(input("enter the num of fibonacci terms : "))
count = 0
i=0
next=1
fib = []
while count<a:
    fib.append(i)
    print(i)
    temp=i+next
    i=next
    next=temp
    count+=1

a=int(input("enter the factorial num : "))

#using recursive function


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("enter number of terms : "))
print("Fibonacci series:")

for i in range(n):
    print(fib(i), end=" ")

#prime num
n=int(input("enter the num : "))
i=2
a=True

while i<=n-1:
    if n%i==0:
        a=False
        break
    i+=1
if a==True:
    print("it is prime ")
else:
    print("it is not prime")
    