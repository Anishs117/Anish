"""import math
a = int(input("enter the 1st number"))
b = int(input("enter the 2st number"))
c = int(input("enter the 3st number"))
if a==0:
    print("error: 'a' cannot be zero")
else:
    discriminant= b**2 - 4*a*c
    if discriminant<0:
        print("error:root are complex.")
    else:
        root1 =(-b + math.sqrt(discriminant)) /(2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Root1:",root1)
        print("Root2:", root2)
 #Q3
sentence = input("Enter your sentence")
letter_count=0
digit_count=0
for char in sentence:
    if char.isalpha():
        letter_count +=1
    elif char.isdigit():
        digit_count+=1
print("letters",letter_count)
print("letters",digit_count)"""
#Q2
sentence = input("entere a sentence")
word= sentence.split()
print (word)

count1 = sentence.count("t")
print (count1)
