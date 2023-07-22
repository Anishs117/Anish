ist=[]
for i in range (2000,2500):
    if (i%5==0 and i%8==0):
        list.append(i)
        print(i)
#Q2
a=int(input("enter a number"))`
for i in range( 1,11):
    j=(i*a)
    print(i,"*",a,"=",j)
#Q3
a=input("enter a word")
b= a.split()
b.sort()
print("the asscending order is",b)
#Q4
a=(input("enter a number"))
b= a.split()
b.sort()
print("the second largest number is",b," ",b[-2])
#Q5
a=[1,2,3,4,5,6,7,8,9,10]
evennum=[]
oddnum=[]
for i in a:
    if (i%2 ==0 ):
        evennum.append(i)
    else:
        oddnum.append(i)
print(evennum,oddnum)
#Q6
b=[]
User = input("enter a number ")
b = User.split()
n = b[::-1]
print(n)
#Q7
b=[]
for i in range(1,51):
     if i%2!=0:
        b.append(i)
     else:
         continue
print(b)
#Q8
even=[]
odd=[]
n=[]
user= (input("enter number"))
l= user.split()
for i in l:
    if int(i)%2==0:
        even.append(i)
    elif int(i)%2!=0:
        odd.append(i)
print(even,odd)