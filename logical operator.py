Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=2
>>> print(a>b&&b>a)
SyntaxError: invalid syntax
>>> (a>b&b>a)
False
>>> (a>b||b>a)
SyntaxError: invalid syntax
>>> (a>b|b>a)
False
>>> a!b
SyntaxError: invalid syntax
>>> not a==b
True
