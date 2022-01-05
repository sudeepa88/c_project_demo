Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=["Sudeepa","Suparna"]
>>> b=[" ","ODI"]
>>> i="\n".join(b)
>>> print(a+i+b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a+i+b)
TypeError: can only concatenate list (not "str") to list
>>> print(i)
 
ODI
>>> print(i+i)
 
ODI 
ODI
>>> j="\t".join(a)
>>> print(j)
Sudeepa	Suparna
>>> print(j+i)
Sudeepa	Suparna 
ODI
>>> k="\t".join(b)
>>> print(k)
 	ODI
>>> print(i+k)
 
ODI 	ODI
>>> print(j+i+k)
Sudeepa	Suparna 
ODI 	ODI
>>> 