#initial basic intro by showing how simple and effevtive python is

#basic math
12+13
25

13-12
1

12/2
6.0

13//2
6

2**3
8

#First programme hello world

print("hello world!")

#Display all keywords so that they will know them and avoid using them as identifiers/variables
#Explain the 5 rules of declering variables
'''

1. Identifiers can be a combintion of letters in lower case (a-z) and upper case (A-Z) or digits (0-9) or an
   uderscore _ 

2. An identifier cannot start with a digit

3. Keyword cannot be used as a variable

4. Identifier will not have any special characters apart from _

5. Identifier can be of any length

'''

var1=10
var1
10

name = "alpha"
age = 26.4

print(name,age)
alpha 26.4

#explain how python takes the datatype using type function

type(name)
<class 'str'>

# swap 2 numbers

#show them how to add comments so that they will have quality understandable code throughout
 #  this is a single line comment

'''
this is a
multi
line
comment
'''

#teach them how to take inputs
#input treates everything as string
val1=input('enter a value: ',)
enter a value: 12
type(val1)
<class 'str'>

#type converting
val2=int(input('enter a value',))

#reading multiple inputs at a time
a,b=input('enter 2 values: ',).split()
enter 2 values: 12 13
a
'12'
b
'13'

#conditional statement
i = 1
if i == 1:
    print("yes i is equal to zero") 
yes i is equal to zero

i='3'
if i == 1:
    print('one')
elif i == 2:
    print('two')
else:
    print('three')

'three'

#find biggest among 3 numbers

#looping statements
#for loop
for i in range(0,10):    #explain in key word and also range
     print(i)
 
0
1
2
3
4
5
6
7
8
9

#while loop
i=0
i=10
while i>0:
    print(i)
    i-=1

10
9
8
7
6
5
4
3
2
1

#list

a=[10,4,57,8.7,7,'ROFOS']
a
[10,4,57,8.7,7,'ROFOS']

#slicing
a[0]
10

a[-1]
'ROFOS'

a[0:2]
[10,4]

a[::-1]
['ROFOS',7,8.7,57,4,10]

#array built in functions pop, insert, append, sort, remove

#reverse sort a list
list1=[12,3,323,332,45,35,6,34]
list1.sort(reverse=True)
list1
[332, 323, 45, 35, 34, 12, 6, 3]

#string
s='Free as in freedom'

s.split()
['Free','as','in','freedom']

s[0]
'f'

s[2:7]
ee as

#Reverse a string
string1="Hello every one!"
string1[::-1]
'!eno yreve olleH'

#print alternative characters in a string
string2="some string"
string2[::2]
'sm tig'


#tuple and dictionaries then wind off

#fizz and buss programme if number is divisible by 3 print fizz. if by 5 print buzz if by both print fizzbuzz

#print prime numbers from 1 to 20
for i in range(1,21):
    for j in range(2,i):
            if i%j==0:
                    break
    else:
            print(i)

#exercise / home work print a food menue using dictionary and its functions
'''
example:
RICE
	 1 white rice
	 2 biryani
Chats
	 1 panipuri
	 2 gobi
'''
menu={'RICE':{1:'white rice', 2:'biryani'},'Chats':{1:'panipuri',2:'gobi'}}
menu
{'RICE': {1: 'white rice', 2: 'biryani'}, 'Chats': {1: 'panipuri', 2: 'gobi'}}
for key,value in menu.items():
    print(key)
    for i,j in value.items():
            print(i,j)


#day 2 content

'''def add():
    a=int(input('enter a value : ',))
    b=int(input('enter 2nd value : ',))
    print('sum = ',a+b)

option=int(input('enter 1 if you want to add 2 numbers : '))
if option==1:
    add()'''
def add(a,b):
    return a+b

option = int(input('enter 1 if you want to add 2 numbers : '))
if option==1:
    c=int(input('enter a number : ',))
    d=int(input('enter 2nd number : '))
total= add(c,d)
print('sum = ',total)

