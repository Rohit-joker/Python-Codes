# from tkinter import *
# from tkinter.ttk import *
# from time import strftime

# root = Tk()
# root.title("clock")

# def time():
#     string = strftime('%H:%M:%S %p')
#     label.config(text=string)
#     label.after(1000,time)

# label = Label(root, font=("ds-digital",80),background = "black" , foreground = "cyan")
# label.pack(anchor='center')
# time()

# mainloop()

# first = input("enter first number ")
# operator = input("enter operator +,-,*,%,/ ")
# second = input("enter second number ")

# first = int(first)
# second = int(second)
# if operator == "+":
#     print(first+second)
# elif operator == "-":
#     print(first-second)
# elif operator == "/":
#     print(first/second)
# elif operator == "*":
#     print(first*second)
# elif operator == "%":
#     print(first%second)
# else:
#     print("invalid operator")

# light=input("enter signal light color :")

# if(light=="green"):
#     print("Go")
# elif(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look")
# else:
#     print("light is broken")

# str1 = "rohit"
# print(str1[4])
# str = "apna college"
# print(str[-5:-1])
#str = "i am studying python from apnacollege"
# print(str.endswith("ege"))
# print(str.capitalize())
# print(str.replace("o","a"))
#print(str.find("o"))
#print(str.count("a"))
# age = input("enter the age :")
# if(int(age)>=18 and int(age)<=100):
#     print("can vote ")
#     print("can drive")
# elif(int(age)<=18 and int(age)>=4):
#     print("on the education")
# elif(int(age)<=4 and int(age)>=0):
#     print("there is child")
# else:
#     print("invalid input")

# marks=[45,54,65,56]
# print(marks)
# print(type(marks))
# print(len(marks))
# #list stores any type of data type
# marks[0]=76
# print(marks)
# print(marks[1:4])
# marks.append(4)
# print(marks.sort())
# print(marks)

#tuple=()
# print(type(tuple))
# movies=[]
# m1=input("enter the name of favorite movie 1 : ")
# m2=input("enter the name of favorite movie 2 : ")
# m3=input("enter the name of favorite movie 3 : ")
# movies=[m1,m2,m3]
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)

"""list=[1,2,3]
print(list)
copylist=list.copy()
copylist.reverse()
if(copylist == list):
    print("palindrome")
else:
    print("not palindrome")"""

# a=int(input("enter the num of fibonacci terms : "))
# count = 0
# i=0
# next=1
# fib = []
# while count<a:
#     fib.append(i)
#     print(i)
#     temp=i+next
#     i=next
#     next=temp
#     count+=1

# a=int(input("enter the factorial num : "))

# fact=1
# count=1

# for count in range(1,a+1):
#     print(count)
#     fact=fact*count
#     count+=1

# print(fact)

# i=5
# while i>=0:
#     k=1
#     while k<=i:
#         print("*",end=" ")
#         k+=1
#     print("\n",end="")
#     i-=1


# num=[1,2,3,4,5,6]

# a=int(input("enter any num you want to search : "))
# idx=0
# while idx<=len(num):
#     if a==num[idx]:
#         print(num[idx])
#         print("Found at index", idx)
#         break
#         exit()
#     else :
#         print("not found ")
#     idx+=1

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)

# n = int(input("enter number of terms : "))
# print("Fibonacci series:")

# for i in range(n):
#     print(fib(i), end=" ")

# def fac(n):
#     if n==0 or n==1:
#         print(n)
#         return 1
#     else:
#         print(n)
#         return n*fac(n-1)
    

# n=int(input("enter num that generate factorial : "))
# result=fac(n)
# print("the fact num is : ",result)

# n = int(input("Enter the number: "))
# i = 2
# a = True

# while i <= n - 1:
#     if n % i == 0:
#         a = False
#         break
#     i += 1

# if a == True:
#     print("It is a prime number")
# else:
#     print("It is not a prime number")