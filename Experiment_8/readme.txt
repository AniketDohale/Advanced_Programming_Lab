Python Multithreading

# Content:
-> Threads Vs Processes
-> Threads and Python: Global Interpreter Lock, Exiting Threads, Accessing Threads
   from Python, Python Threading Modules
-> The thread Module
-> The threading Module

# Aim:
- Write a python program with a function that obtains a byte value and a filename
(as parameters or user input) and displays the number of times that byte appears in the
file. Suppose now that the input file is extremely large. Multiple readers in a file is
acceptable, so modify your solution to create multiple threads that count in different
parts of the file such that each thread is responsible for a certain part of the file. Collate
the data from each thread and provide the correct total. Use the timeit module to time
Both the single-threaded and new multithreaded solutions and say something about the
difference in performance, if any.