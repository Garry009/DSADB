Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a[1,2,3]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a[1,2,3]
NameError: name 'a' is not defined
a=[1,2,3]
type(a)
<class 'list'>
a.append(1,/)
SyntaxError: invalid syntax
a.append(1)
print(a)
[1, 2, 3, 1]
a.clear()
a.append(1,2,3,4,6)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.append(1,2,3,4,6)
TypeError: list.append() takes exactly one argument (5 given)
a.append([1,2,3,4,6])
print(a)
[[1, 2, 3, 4, 6]]
a.append(2)
print(a)
[[1, 2, 3, 4, 6], 2]
b=[1,2,3]
a.copy(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.copy(b)
TypeError: list.copy() takes no arguments (1 given)
a=b
print(a)
[1, 2, 3]
a=b.copy()
print(a)
[1, 2, 3]
c=[1,23,4,5,68]
c=b.copy()
c.count()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c.count()
TypeError: list.count() takes exactly one argument (0 given)
c.count(1)
1
c.count(23)
0
d=[1,2,1,2,1,2,1,2,2,3,4,4,4]
d.count(1)
4
d.extend(c)
print(d)
[1, 2, 1, 2, 1, 2, 1, 2, 2, 3, 4, 4, 4, 1, 2, 3]
print(c)
[1, 2, 3]
d.index(








    ;
    
SyntaxError: '(' was never closed
d.insert(20,2);
    
print(d)
    
[1, 2, 1, 2, 1, 2, 1, 2, 2, 3, 4, 4, 4, 1, 2, 3, 2]
d.insert(2,20)
    
print(d)
    
[1, 2, 20, 1, 2, 1, 2, 1, 2, 2, 3, 4, 4, 4, 1, 2, 3, 2]
print(d.pop())
    
2
d.remove(2)
    
d
    
[1, 20, 1, 2, 1, 2, 1, 2, 2, 3, 4, 4, 4, 1, 2, 3]
d.reverse()
    
d
    
[3, 2, 1, 4, 4, 4, 3, 2, 2, 1, 2, 1, 2, 1, 20, 1]
d.sort()
    
d
    
[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 20]
b={}
    
type(b)
    
<class 'dict'>
d=b.fromkeys('lion','king')
    
b
    
{}
d
    
{'l': 'king', 'i': 'king', 'o': 'king', 'n': 'king'}
c=b.fromkeys('hello',[1,2,3,4,5])
    
c
    
{'h': [1, 2, 3, 4, 5], 'e': [1, 2, 3, 4, 5], 'l': [1, 2, 3, 4, 5], 'o': [1, 2, 3, 4, 5]}
d.get(h)
    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d.get(h)
NameError: name 'h' is not defined
d.get('h')
    
print(d.get('h'))
    
None
c
    
{'h': [1, 2, 3, 4, 5], 'e': [1, 2, 3, 4, 5], 'l': [1, 2, 3, 4, 5], 'o': [1, 2, 3, 4, 5]}
c.get('h')
    
[1, 2, 3, 4, 5]
a=[1,2,3,4]
    
type(a)
    
<class 'list'>
a.pop()
    
4
a
    
[1, 2, 3]
c
    
{'h': [1, 2, 3, 4, 5], 'e': [1, 2, 3, 4, 5], 'l': [1, 2, 3, 4, 5], 'o': [1, 2, 3, 4, 5]}
c.items()
    
dict_items([('h', [1, 2, 3, 4, 5]), ('e', [1, 2, 3, 4, 5]), ('l', [1, 2, 3, 4, 5]), ('o', [1, 2, 3, 4, 5])])
x=[1,2,3,4,5]
    
x[2]
    
3
x.insert(2,7)
    
x
    
[1, 2, 7, 3, 4, 5]
x*5
    
[1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5, 1, 2, 7, 3, 4, 5]
x.remove(4)
    
x
    
[1, 2, 7, 3, 5]
for i in x:;
    
SyntaxError: invalid syntax
for i in x:
    print(i)
... 
1
2
7
3
5
>>> x.sort
...     
<built-in method sort of list object at 0x000001A2304A1140>
>>> x.sort()
...     
