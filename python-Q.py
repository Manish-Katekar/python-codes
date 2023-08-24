'''
WAP to print the odd numbers from 1 to 99. Prints one number per line.

WAP  to accept a number and check the number is even or not. Prints 1 if the number is even or 0 if the number is odd.

WAP to print numbers between 1 to 100 which are divisible by 3, 5 and by both
( total 3 list of numbers to be printed)

WAP that accepts three integers from the user and return true if two or more of them (integers ) have 
the same rightmost digit. The integers are non-negative

WAP to convert input number of seconds to HH:MM:SS.

WAP to print all leap years between 2000 to 2100. Apply all conditions of checking leap year ( (divisible by 4 and not divisible by 100) OR (divisible by 400))

WAP to print calender for a month. Take how many days are there in month and starting day of the month as input
    Ex. input no of days : 30  starting day of month : Thursday
    Ouput :: Day wise Calender  ( just like June 2022 month)

WAP to print day of input date when given day for 1st day of that month
    ex. input date : 16/07/2022  day of 1st day of that month : Friday
    output : saturday
'''
#1
for i in range (1,101):
    if(i%2!=0):
        print(i)

#2
n=int(input("Enter a number:"))
if(n%2==0):
    print("even number")

#3
l1=[]
l2=[]
l3=[]

for i in range(1,101):
    if (i%3==0):
        l1.append(i)
    if(i%5==0):
        l2.append(i)
    if(i%3==0 and i%5==0):
        l3.append(i)
    
print("Numbers divisible by only 3:",l1)
print("Numbers divisible by only 5:", l2)
print("Numbers divisible both 3 and 5:", l3)

#4
l1=[]
for i in range(3):
    n1=int(input("Enter 1 of 3 positive integer:"))
    r1=n1%100
    r2=r1%10
    print(r2)
    l1.append(r2)
if (l1[0]==l1[1] or l1[0]==l1[2] or l1[1]==l1[2] ):
    print("True")

else:
    print("False")


#5
# Take input from user
total_seconds = int(input("Enter number of seconds: "))

# Calculate hours, minutes and seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Format output as HH:MM:SS
time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Print output
print("Time in HH:MM:SS format: ", time_string)


#6
for i in range(2000,2101,1):
    if(i%4==0):
        if(i%100==0):

            if(i%400==0):
                print("leap-",i)
            else:
                print("not leap-",i)
        else:
            print("leap",i)

    else:
        print("not leap-",i)

#7

# Get input values from user
num_days = int(input("Enter the number of days in the month: "))
start_day = input("Enter the starting day of the month (e.g. Monday): ")

# Define a list of weekdays
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Find the index of the starting day
start_day_index = weekdays.index(start_day.title())

# Print the header of the calendar
print(" " * 6, "Calendar", " " * 6)
print(" " * 4, "Month of the year")
print("Mo  Tu  We  Th  Fr  Sa  Su")

# Print the days of the month
for i in range(start_day_index):
    print("   ", end="")
for i in range(1, num_days+1):
    #print("{:02d}".format(i), end=" ")
    print(f"{i:02d}", end="")
    if (i + start_day_index) % 7 == 0:
        print()
    elif i == num_days:
        print("\n")
    else:
        print(" ", end="")


"""
WAP to print day of input date when given day for 1st day of that month
    ex. input date : 16/07/2022  day of 1st day of that month : Friday
    output : saturday
"""
import calendar

def get_day_of_input_date(input_date, first_day):
    # Convert input date to a list of day, month, and year
    day, month, year = map(int, input_date.split('/'))

    # Get the day index of the first day of the month (Monday = 0, Sunday = 6)
    first_day_index = calendar.day_name.index(first_day.capitalize())

    # Get the day index of the input date
    input_day_index = calendar.weekday(year, month, day)

    # Calculate the difference in days between the input date and the first day of the month
    day_difference = (input_day_index - first_day_index) % 7

    # Calculate the day of the input date based on the first day of the month
    input_day = calendar.day_name[(first_day_index + day_difference) % 7]

    return input_day

# Example usage
input_date = "16/07/2022"
first_day = "Friday"
day_of_input_date = get_day_of_input_date(input_date, first_day)
print(day_of_input_date)



'''
Check Palindrome number

Check Palindrome string.

Find duplicate characters in a string.

Permutation and Combination Program

Pattern Programs --> star patterns

print table of any given number 
    2,4,6,8,10,12,14,16,18,20
'''
#1,2

num=input("Enter a number:")
if(num==num[::-1]):
    print("Plindrome number")
else:
    print("Not a plindrome")

#3   cook

s1=input("Enter a string:")
s2=list(s1)

l2=[]
for i in range(len(s2)):
    if(s2[i] not in l2[:]):
        for j in range(i+1,len(s2)):
            if(s2[i]==s2[j]):
                l2.append(s2[i])
                break
l2.remove(" ")
print("Duplicate characters are : ",l2)

"""
2.	Print the following patterns using loop : 
a. 
* 
** 
***
****
b. 
    *                    
  ***                
***** 
  ***
    * 
c. 
1010101          
 10101  
  101   
   1    

d.
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5 
"""
#
for i in range(4):
    i+=1
    print("*"*i)

#
for i in range(5):
    i+=1
    for j in range(i):
        j+=1
        print(j,end="")
    print("")
#
n=int(input("Enter a odd number:"))
space=n-1   
star=1
a=(n//2)+1
for i in range(a):

    print(" "*space,end="")
    print("*"*star)
    if(i==(a-1)):
        break
    space-=2
    star+=2

space+=2
star-=2
for j in range(a-1):
    print(" "*space,end="")
    print("*"*star)
    space+=2
    star-=2

"""
*******
 *****
  ***
   *

1010101          
 10101  
  101   
   1    
"""

n=int(input("Enter a odd number:"))
space=0
for i in range(n):
    print(" "*space+"*"*n)
    n-=2
    space+=1

##
n=int(input("Enter a odd number:"))
space=0
pattern=n-1
for i in range(n):
    print(" "*space,end="")
    print("1",end="")
    print("01"*pattern)
    n-=2
    space+=1
    pattern-=1

#table print
num=int(input("Enter a number:"))
print(f"Table of {num} is ")
for idx in range(1,11):
    
    print(f"{num} X {idx} = {num*idx}")




#Write a  program that takes three numbers as input then print maximum and minimum number of the three
#bubble sort

length=int(input("Enter number of elements want to sort:"))
l1=[]
for i in range(length):
    l1.append(int(input(f"Enter {i+1} number:")))
print(l1)
for idx in range(length-1):
    for j in range(len(l1)-1):
        if(l1[j]>l1[j+1]):
            l1[j], l1[j + 1] = l1[j + 1], l1[j]   ########################_very important
        else:
            continue
print(l1)
print(f"maximum number is {l1[length-1]}")
print(f"minimum number is {l1[0]}")

"""
N = int(input())
data = [int(x) for x in input().split()]

print(data)
------------------->inputs in sigle line
"""
#Write a  program to swap two variables

def swap(a,b):
    a,b=b,a
    return a,b

c=3
d=10
d,c= swap(d,c)
print(d-c)

#or
a=input()
b=input()
a,b=b,a
print(a,b)

#WAP to calculate distance between two points-------------------------------
import numpy as np
point1 = np.array((2,5))
point2 = np.array((5,7))
 
# finding sum of squares
sum_sq = np.sum(np.square(point1 - point2))
 
# Doing squareroot and
# printing Euclidean distance
print(np.sqrt(sum_sq))

#WAP  to count the letters, spaces, numbers and other characters of an input string.
#ascii values--(a-z)=(97-122);   (A-Z)=(65-90);  (0-9)=(48-57)
string=input()
low=0
upp=0
num=0
other=0
space=0
for idx in string:
    if(ord(idx)<=122 and ord(idx)>=97):
        low+=1

    elif(ord(idx)<=90 and ord(idx)>=65):
        upp+=1

    elif(ord(idx)<=57 and ord(idx)>=48):
        num+=1
    
    elif(idx==" "):
        space+=1

    else:
        other+=1

print(f"no of spaces={space} \nno. of numbers={num} \nno. of characters={low+upp}\nremaining characters={other}")


# calculate filesize
import os

filename = "C:/Users/manis/OneDrive/Desktop/python exercises/py_exercise_folder/IACSDassignment/100+ques/example.txt"
size = os.path.getsize(filename)

print(f"The size of {filename} is {size} bytes.")

#time format
import datetime

now = datetime.datetime.now()
time = now.strftime("%H:%M:%S")

print(f"The current system time is {time}.")


########
import datetime

now = datetime.datetime.now()
date_time = now.strftime("%y-%m-%d %H:%M:%S")

print(f"The current date time is {date_time}.")

#WAP to accepts an integer and count the factors of the number.

num=int(input("Enter an integer:"))
count=0
for idx in range(num):
    idx+=1
    if(num%idx==0):
        print(idx)
        count+=1
print(f"No. of factors of {num} is {count}")

"""
WAP to capitalize the first letter of each word in input sentence.

WAP to find the penultimate (last but one) word of a sentence.

WAP to check if input is 4 digit number and less than 3000

WAP to find second last maximum value

WAP to find second last minimum value

WAP to find number in a list which is repeated exactly 'n' times
"""
#
sentence=input("Enter a sentence:")
a=sentence.title()
print(a)

#
sentence=[idx for idx in input().split()]
print(sentence)
print(sentence[-2])

#
n=input("Enter a number:")
if(len(n)==4 and int(n)<3000):
    print("valid")
else:
    print("invalid")

#
l1=[int(idx) for idx in input().split()]

for i in range(len(l1)-1):
    for j in range(len(l1)-1):
            if(l1[j]>l1[j+1]):
                l1[j+1],l1[j]=l1[j],l1[j+1]
            
print(l1)
print(f"second max number is {l1[-2]}")
print(f"second min number is {l1[1]}")

#
s1=input("Enter a string:")
s2=list(s1)

l2=[]
for i in range(len(s2)):
    if(s2[i] not in l2[:]):
        for j in range(i+1,len(s2)):
            if(s2[i]==s2[j]):
                l2.append(s2[i])
                break
l2.remove(" ")
print(l2)
print(len(l2))
dic={}
for id in l2:
    count=0
    for jd in range(len(s2)):
        if(id==s2[jd]):
            count+=1
    dic[id]=count

print(dic)
repeat=int(input("repeatation: "))
for key, value in dic.items():
    if value == repeat:
        print(key)

"""

WAP to insert a word in the middle of the another string. 
    EX. Insert "Tutorial" in the middle of "Python 3.9", so result will be Python Tutorial 3.9

WAP to extract the first half of a given string

WAP to create a string in the form short_string + long_string + short_string from two strings. Give error if strings same length.

WAP  to create the concatenation of the two strings except removing the first character of each string. The length of the strings must be 1 and above

WAP to create a new string taking first three characters from a given string. If the length of the given string is less than 3 use "#" as substitute characters

"""

#
print("Enter a string having even no of words:")
string=[item for item in input().split()]
print(string)
word=input("Enter a word to insert:")
index=(len(string)//2)
string.insert(index,word)
print(string)
print(" ".join(string))

#
print("Enter a string having even no of words:")
string=[item for item in input().split()]
print(string)
index=(len(string)//2)
print(" ".join(string[:index]))

#
s1=input("Enter first string:")
s2=input("Enter second string:")

if len(s1)<len(s2):
    print(s1+" "+s2+" "+s1)


elif len(s2)<len(s1):
    print(s2+" "+s1+" "+s2)

else:
    print("error : strings are equal")

#formating see
def concatenate(s1,s2):
    return "{} {}".format(s1, s2)

s1=input("Enter first string:")
s2=input("Enter second string:")
print(concatenate(s1,s2))


#ljust rjust

string=input()
if len(string)>=3:
    print(string[:3])
else:
    s=string.ljust(3,"#")
    print(s)

"""
WAP to take file name with any extension as input. Print name and extension of the file name seperately.
    ex. my_photo.png    --> name : my_photo ext: png
        myfile.docx     --> name: myfile  ext: docx
        1.gz            --> name: 1  ext:gz

WAP to check if a string starts with a specified word. 
Sample Data: string1 = "Hello how are you?"
word = "Hello"
Sample Output: True

WAP to sort array of strings based on alphabetical order of second character of each string. 
Assume all strings are minimum 2 character long

WAP to find all strings in an array of strings which end with "g" or start with "p"

WAP  start with an input integer n, divide n by 2 if n is even or multiply 
by 3 and add 1 if n is odd, repeat the process until n = 1.


"""
#
filename=input("Enter a filename with its extension:")
l1=filename.split(".")
print(f"Name: {l1[0]} ; Extension: {l1[1]}")

#

string=[item for item in input().split()]
word=input("Enter word start with:")
if(string[0]==word):
    print("True")
else:
    print("False")

#
string = [item for item in input().split()]
for i in range(len(string)):
    for j in range(i+1, len(string)):
        if string[i][1] > string[j][1]:
            temp = string[i]
            string[i] = string[j]
            string[j] = temp
        else:
            continue

print(string)

""" or
lambda----->
The loop is actually hidden inside the sorted() function. When sorted() is called with a list as its argument, it internally iterates over each element of the list and compares them to each other based on the key parameter.

In this case, the key parameter is a lambda function lambda x: x[1],
which takes a string x as its argument and returns the second character of the string.
So, when sorted() iterates over each element of the list,
it calls the lambda function with each element as its argument to determine the value to sort by.
"""

string = [item for item in input().split()]
sorted_string = sorted(string, key=lambda x: x[1])
print(sorted_string)



#end with g start with p
string = [item for item in input().split()]
l1=[]
for item in string:
    if(item[0]=='p' and item[-1]=='g'):
        l1.append(item)
    
print(l1)
for word in l1:
    print(word,end=" ")

#
n = int(input("Enter an integer: "))
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)

"""
WAP to test if 10 appears as either the first or last element of an array of integers. 
The length of the array must be greater than or equal to 2.

WAP to test if the first or the last element of two array of integers are same. 
The length of the array must be greater than or equal to 2.

WAP to merge two arrays into a single array. First element from first array then 
first from second array like wise. 

WAP to do right shift on given integer.
    Ex. val = 1234 after right shift
        right_shifted_val = 4123

WAP to do left shift on given integer.
    Ex. val = 1234 after right shift
        left_shifted_val = 2341


WAP to read an integer and calculate the sum of its digits and 
write the number of each digit of the sum in English.
    Ex. 1234 --> output "One Zero"
        999999999999 --> output "One Zero Eight"


WAP given a list of numbers create two lists one which contains all numbers divisible by 5 
and another list for remaining numbers

WAP to count the number of even and odd elements in a given array of integers.

"""
#
array=[int(idx) for idx in input().split()]
if(array[0]==10 and array[-1]==10):
    print("List has 10 at start and at end")
else:
    print("Not satisfy")


#

array1=[int(idx) for idx in input("Enter first array:").split()]
array2=[int(idx) for idx in input("Enter second array:").split()]
if(array1[0]==array2[0] and array1[-1]==array2[-1]):
    print("first and last elements of two arrays are same")
else:
    print("Not same")

#
array1=[int(idx) for idx in input("Enter first array:").split()]
array2=[int(idx) for idx in input("Enter second array:").split()]

l1=[]
for i in range(len(array1)):
    l1.append(array1[i])
    for j in range(i,i+1):
        l1.append(array2[j])

print(l1)

#
n=input("Enter a number:")
a=n[-1]+n[0:-1]
print(a)


#
n=input("Enter a number:")
a=n[1:]+n[0]
print(a)


#
words={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
n=input("Enter a number:")
sum=0
for digit in n:
    sum+=int(digit)
print(sum)
a=list(str(sum))

for i in a:
    print(words[int(i)],end=" ")

#
l=[10,5,78,6,74,65,87,35]
l1=[]
l2=[]
for item in l:
    if(item%5==0):
        l1.append(item)
    else:
        l2.append(item)

print(f"list contains elements divisible by five {l1} \nRemaining elements {l2}")

#
l=[10,5,78,6,74,65,87,35]
l1=[]
l2=[]
for item in l:
    if(item%2==0):
        l1.append(item)
    else:
        l2.append(item)

print(f"list contains Even elements {l1} \nlist contains Odd elements {l2}")

"""
WAP to check if an array of integers contains two consecutive occurances of 10 or 20 but not both
    ex. [10,30,50,10,10 ]  --> True
        [20,20,89,67] --> True
        [10,10,20,20] --> False
        [23,10,34,10,56] --> False
        [23,20,34,20,56] --> False

WAP to find unique numbers in an array and count their occurance.

WAP to find unique words in a sentence and count their occurance.

WAP to find unique characters in a sentence and count their occurance.

WAP to check if an array of integers contains three increasing adjacent numbers
    ex. [1,3,5,2,5] --> True
        [1,1,4,2,67,5] --> False
        [1,9,2,67,100,124,34] --> True
"""
#
array=[int(idx) for idx in input().split()]
count10=0
count20=0
for indx in range(len(array)-1):
    if(array[indx]==10 and array[indx+1]==10):
        count10+=1
    elif(array[indx]==20 and array[indx+1]==20):
        count20+=1


if(count10>=1 and count20==0):
    print(True)
elif(count10==0 and count20>=1):
    print(True)
else:
    print("False")

#
numbers=[int(idx) for idx in input().split()]
l1=[]
l2=[]
for item in numbers:
    if (item not in l1):
        l1.append(item)
    elif(item in l1):
        l2.append(item)
s1=set(l1)
s2=set(l2)
print(s1-s2)
print(f"number of unique digits is {len(s1-s2)}")

#
sentence=[idx for idx in input().split()]
l1=[]
l2=[]
for word in sentence:
    if (word not in l1):
        l1.append(word)
    elif(word in l1):
        l2.append(word)
s1=set(l1)
s2=set(l2)
print(s1-s2)
print(f"number of unique words is {len(s1-s2)}")

#
sentence=[idx for idx in input().split()]
l1=[]
l2=[]
for word in sentence:
    for char in word:
        if (char not in l1):
            l1.append(char)

        elif(char in l1):
            l2.append(char)

s1=set(l1)
s2=set(l2)
print(s1-s2)
print(f"number of unique characters is {len(s1-s2)}")    

#
array=[int(idx) for idx in input().split()]

for i in range(len(array)-2):
    if(array[i]<array[i+1]<array[i+2]):
        a=True
    else:
        a=False
    
if(a==True):
    print("True")
else:
    print("False")


'''
Factorial Program using Recursion
    n! = n * (n-1) * (n-2) * ... *2*1

Factorial of a number using loop
    n! = n * (n-1) * (n-2) * ... *2*1

Fibonacci Series.
    1,1,2,3,5,8,13,21,34,...

Armstrong Number.
    It is a number with 'n' digits. Here (sum of every digit ^ n) equal to ( number itself)

    1) 1^3 5^3 3^3=153 ( here number of digits(n) is 3)
    2) 1^1 = 1 ( here number of digits is 1)
    3) 1634 = 1^4 + 6^4 + 3^4 + 4^4 ( here number of digits is 4)


Perfect number.

Prime number.
    Number is not divisible by any number other than 1 and itself

Reverse a string.

Reverse a number.
'''


#1
fact=1
num=int(input("Enter a number:"))
for i in range(num):
    i+=1
    fact=fact*i

print(fact)

#2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter a number:"))
print(factorial(n))



#3
# Get input from user for number of terms in the sequence
num_terms = int(input("Enter the number of terms in the sequence: "))

# Initialize the first two terms of the sequence
prev_num = 0
curr_num = 1

# Print the first two terms
print(prev_num)
print(curr_num)

l1=[0,1]
# Generate and print the remaining terms
for i in range(2, num_terms):
    next_num = prev_num + curr_num
    
    prev_num = curr_num
    curr_num = next_num
    l1.append(next_num)
print(l1)    

#logic --> (0,1)1,(1,1)2,(1,2)3,(2,3)5,(3,5)8,(5,8)13,(8,13)21,(13,21)34

#4
num=input("Enter a number:")
n=len(num)
sum=0
for i in num:
    sum=sum+int(i)**n

if(sum==int(num)):
    print("Given number is Armstrong Number")
else:
    print("Not an Armstrong Number")

#5
count=0
num=int(input("Enter a number:"))
for i in range(num):
    i+=1
    if(num%i==0):
        count+=1
if(count==2):
    print("prime number")
else:
    print("Not a Prime number")

#6
sum=0
num=int(input("Enter a number:"))
for i in range(1,num):
    if(num%i==0):
        sum+=i

if(sum==num):
    print("Perfect number")
else:
    print("Not a perfect number")


#7
num=input("Enter a number:")
print(num[::-1])

#8
num=input("Enter a number:")
print(num[::-1])









