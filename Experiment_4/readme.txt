Python Modules and Packages

# Content:
-> Modules: Python Program Architecture, Module Search Path
-> Module Codding Basics: Module Creation, Module Usage, Module Namespaces
-> Module Packages: Package Import Basics, Package Relative Imports
-> Advanced Module Topics: Module Design Concepts, Data Hiding in Modules, Mixed Usage Modes

# Aim:
Write a Python Program that counts the lines and characters in a file (similar in spirit to part of
what wc does in Unix). With your text editor, code a Python module called mymod.py that exports three-top level names:
a) A count Lines(name) function that reads an input file and counts the number of lines in it 
(hint: file.readlines does most of the work for you, and len does the rest, 
though you could count with for and file iterators to support massive filestoo).

b) A count Chars(name) function that reads an input file and counts the number of characters in it 
(hint: file.read returns a single string, which may be used in similar ways).

c) A test(name) function that calls both counting functions with a given input filename. 
Such a filename generally might be passed in, hardcoded, input with the input built-in function