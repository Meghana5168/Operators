Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
##membership operators
print(2in[1,2,3,4,5])
True
print(6 in [1,2,3,4,5])
False
print(6 not in [1,2,3,4,5])
True
print(2 not in [1,2,3,4,5])
False
print(6 not in "abc")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(6 not in "abc")
TypeError: 'in <string>' requires string as left operand, not int
print("d" not in "abc")
True
##identity operator
##.is ..is not
num=10
print(id(num))#printing the refferencr address
140728930354376
num1=10
num2=10
print(id(num1))
140728930354376
print(id(num2))
140728930354376
print(num1 is num2)
True
li=[1,2,3,4]
l2=[1,2,3,4]
print(li is l2)
False
print(id(li))
2068631608256
print(id(l2))
2068631553088
##defination :it checks the id of the objects and returns boolean values
##defination :it checks the id of the objects and returns boolean values
##BItwise operator
10&2
2
10|2
10
10^2
8
~10
-11
>>10
SyntaxError: invalid syntax
>10
SyntaxError: invalid syntax
10>>
SyntaxError: invalid syntax
10>>1
5
10<<1
20
##Strings
s='abcde'
#indexing
print(s[0])
a
print(s[1])
b
print(s[2])
c
#slicing
>>> print(s[1:4])
bcd
>>> print(s[2:3])
c
>>> print(s[1:-4])

>>> print(s[:4])
abcd
>>> print(s[2:-2])
c
>>> print(s[3:5])
de
>>> print(s[::4])
ae
>>> print(s[::2])
ace
>>> ## String reversal using Slicing
>>> print(s[::-1])
edcba
>>> ## String concatination using'+'
>>> s1=COde
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s1=COde
NameError: name 'COde' is not defined
>>> s2='Gnan
SyntaxError: unterminated string literal (detected at line 1)
>>> s1='code'
>>> s2='Gnan'
>>> print(s1+" "+s2)
code Gnan
>>> print(s1+s2)
codeGnan
>>> ## string repetation using '*'
>>> s='meghann'
>>> print(s*6)
meghannmeghannmeghannmeghannmeghannmeghann
>>> ## string case converstion
>>> s='meghana'
>>> print(s.upper())
MEGHANA
>>> print(s.swapcase())
MEGHANA
>>> ##title
>>> print(s.title())
Meghana
