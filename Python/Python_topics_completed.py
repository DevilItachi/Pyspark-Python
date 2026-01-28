1. Numbers
     - Integers = 2,-3
     - Floating = 2.5 , 4E2(4x10^2)
     - abs(), round()

2. Variable assignments
     - dont use l,o,I as variable names as this are confusing
3. Strings
     - single, double , triple quotes to write strings. Double mostly preffered.
     - want to write codes in next line then use triple single/double codes or you can use  \ at the end of line
     - want \ in text use it 2 times \\
     - # is used for comment
     - use single quotes, when your string has double quotes in it, and vice versa
     - String indexing , slicing , concate(+) 
     - f Strings {} = inserts strings in strings 
     - raw string r' ' ,r means Python will not treat \ as escape characters , Required for regex patterns
     - String functions called Methods var.upper(), var.split(),  var.startswith() , var.endswith() 
     - isupper() , islower() , isnumeric() , isalpha() , isalnum() , capitalize() , upper(), lower(), count(), find()
     - Indendation 4 spaces per indendation
4. Lists
     - can store different datatype []
     - Lists are mutable
     - List indexing , slicing , concate(+) , List methods , nested list
     - List comprehension - creates a NEW list by looping over an iterable and collecting value
     - .append() , .extend() , .insert() , .remove() , .pop() , .clear() , .index() , .count() , .sort() , .reverse() , copy()
     - " ".join(list) # used to join list of strings into a single string
5. Dictionaries
     - key value pairs {}
     - can store different datatype 
     - Dictionaries are mutable
     - Dictionary indexing , slicing , concate(+) , Methods , nested Dictionary
     - .keys(), .values() , .items() , sorted(d.values()) , .get() 
6. Tuples
     - immutable , but similar to List ()
     - If want to modify tuple, convert to list perform operation, convert back to tuple
7. Sets and booleans
     - Sets are an unordered collection of unique elements () . The result of set is in {}
     - List can be converted to set, which will not have duplicates, and again converted back to list
     - union, intersection, difference, issubset, issuperset, etc can be applied on sets.
     - Booleans - with predefined True and False displays that are basically just the integers 1 and 0). It also has a placeholder object called None.
     - add(1) , clear(), clear() , s.difference(sc) , discard(2) , s1.intersection(s2) , s1.isdisjoint(s2) , 
8. Comparison operators
     - output a Boolean value (True or False).
     - == , != , > , <,  >= ,  <=
     - And , Or 
     - abs()
9. Files
     - Python uses file objects to interact with external files on your computer
     - need to install certain libraries or modules to interact with those various file types
     - create file (%%write text.txt), current directory (pwd) , open() , read(), seek(0), readlines() , close(), 
     - write to file open(text.txt , w+)  write()  -- this is truncate and write
     - append to file open(text.txt , a+)  write() -- appends the file
     - Iterating through a file




10. Statements
    - Indentation are important in python, no proper indendation , code will fail
    - if, elif, else , nested if 
                if condition:
                    statement
                elif condition:
                    statement
                else:
                    statement            

    - for loop , apply on list, tuple , dictionary. It just iterates through all the elements given
                for item in list:
                    statement
                
                for itme in list:
                    stament
                    break
                else:        # this else depends on break, if break is not executed, else is executed
                    statement

    - while loop - will repeatedly execute a single statement or group of statements as long as the condition is true
                while test:
                    code statements
                else:           # this else is executed when the while loop is over
                    final code statements
    - break: Breaks out of the current closest enclosing loop.
    - continue: Goes to the top of the closest enclosing loop.
    - pass: Does nothing at all.
                    while x < 10:
                        print("x is currently:", x)
                        print("x is still less than 10, adding 1 to x")
                        x += 1
                        # Do nothing when x == 1 (placeholder)
                        if x == 1:
                            pass
                        # Skip iteration when x == 2
                        elif x == 2:
                            print("Continuing because x == 2")
                            continue
                        # Stop loop when x == 3
                        elif x == 3:
                            print("Breaking because x == 3")
                            break
                        print("End of loop iteration")
                    return "Loop finished"
                
                
11. Useful operators
    - range(start,end,step) - returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
    - enumerate - Enumerate allows you to keep a count as you iterate through an object. It does this by returning a tuple in the form (count,element)
                enumerate() walks through a list and gives you two things at the same time:
                1. Position number (count)
                2. Actual item
                It starts with 0 by default
                for i,letter in enumerate('abcde'):
                    print(f"At index {i} the letter is {letter}")
    -zip -create a list of tuples by "zipping" up together two or more lists. Items are zipped according to same index value.
                mylist1 = [1,2,3,4,5]
                mylist2 = ['a','b','c','d','e']
                list(zip(mylist1,mylist2)) # can use multiple list to pack them in tuple
                - zip() stops at the shortest list , if 2 list sizes are different
                - zip itself creates a zip object so use list(zip())
                - can create list, dict
    - in operator  'x' in ['x','y','z'] = True
    - not in operator 'x' not in ['x','y','z'] = False
    - min and max operator min(mylist) = 1 , max(mylist) =5 
    - random - from random import *  
                - shuffle(mylist)
                - randint(0,100) # generates 1 randoom int including 0 and 100
    - input - takes input from the user,waits (blocks) until the user types something and presses Enter.. By default it will be string.
                - input('Enter Something into this box: ')

12. List Comphrension
    - allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets
                - mylist = [x for x in range(0,11)]
                - lst = [x for x in range(11) if x % 2 == 0]
                - lst = [ x**2 for x in [x**2 for x in range(11)]] # nested list comphrension can also be done

Moudle 3 Methods and Functions
13. List Methods
                - .append() , .extend() , .insert() , .remove() , .pop() , .clear() , .index() , .count() , .sort() , .reverse()
13. Functions
    - a set of statements so they can be run more than once. also let us specify parameters that can serve as inputs to the functions.
    - not have to repeatedly write the same code again and again.
    - return allows a function to return a result that can then be stored as a variable, or used in whatever manner a user wants.
    - Return breaks and exits the function.
    - The return keyword allows you to actually save the result of the output of a function as a variable. The print() function simply displays the output to you, but doesn't save it for future use
    - Tuple unpacking through function
                def employee_check(work_hours):
                    # Set some max value to intially beat, like zero hours
                    current_max = 0
                    # Set some empty value before the loop
                    employee_of_month = ''
                    
                    for employee,hours in work_hours:
                        if hours > current_max:
                            current_max = hours
                            employee_of_month = employee
                        else:
                            pass
                    # Notice the indentation here
                    return (employee_of_month,current_max)
                emp_name = employee_check(work_hours)  # calling a function with parameters
    - Functions often use results from other functions.
    - Functions can be nested as well
    - del hello # deletes a function hello
14. Map Function
     - a loop that applies the same operation to every item in an iterable. takes 1 element at a time and applies function to it
     - It does not execute immediately. It processes items one by one (lazy evaluation)
     - list(map(function, iterable))  # basic syntax for map list
     - list(map(splicer,mynames))
15. filter function
     - you need to filter by a function that returns either True or False
     - filter function returns an iterator yielding those items of iterable for which function(item) is true
     - list(filter(function, iterable)) # basic syntax for filter list
     - list(filter(check_even,nums))
16. Reduce function
     - The function reduce(function, sequence) continually applies the function to the sequence. It then returns a single value.
     - First it will 2 take iterable, solve it and get 1 value, then it will take that value and the next value in the iterable and solve it and get the next value, and so on until it is done with the iterable.
     - reduce(lambda x,y: x+y,lst)
     - reduce(function, iterable)
16. Lambda Expression
     - lambda expressions allow us to create "anonymous" functions. basically means we can quickly make ad-hoc functions without needing to properly define a function using def
     - lambda's body is a single expression, not a block of statements.
     - lambda arguments: expression    # basic syntax 
     - list(map(lambda num: num ** 2, my_nums))
     - not every function can be translated into a lambda expression.
17. Variable Scope
    - LEGB Rule
         - L: Local - Names assigned in any way within a function (def or lambda)
         - E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda) from inner to outer
         - G: Global (module) - Names assigned at the top-level of a module file , or declared global in a def within the file
         - B: Built-in (Python) - Names preassigned in the built-in names module : open,range,SyntaxError -
     -  use the globals() and locals() functions to check what are your current local and global variables.
     - inside function if we write global x and assign new value to x, it will change the global x value
18. *args and **kwargs
     - *args lets a function accept ANY number of parameters.
     - args is just a tuple. The * tells Python to Collect all extra parameters and pack them into one tuple
     - its not necessary we have to use args word, we can use any word but start should be *. eg *spam, *abc. 
                 - def myfunc(*args):
                     return sum(args)*.05
19. **kwargs
     - lets a function accept ANY number of named inputs (key = value) like dictionary
     - kwargs is just a dictionary. The ** tells Python to Collect all extra parameters and pack them into one dictionary
     - its not necessary we have to use kwargs word, we can use any word but start should be **. eg **spam
     - You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs
                - def myfunc(*args, **kwargs):
                     if 'fruit' and 'juice' in kwargs:
                        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
                        print(f"May I have some {kwargs['juice']} juice?")
                     else:
                        pass
                    
                  myfunc('eggs','spam',fruit='cherries',juice='orange')
Palindrome - A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"
Pangrams  - A Pangrams are words or sentences containing every letter of the alphabet at least once.

20. Object oriented programming (OOPS)
     - Writing code by treating real-world things as objects so programs become clean, reusable, and easy to manage
     - OOPS uses 4 main ideas (super simple)
                1. Class -  Blueprint
                👉 Like a design of a car
                2. Object - Real thing
                👉 The actual car made from the design
                3. Encapsulation - Keep things safe
                👉 Don't allow everyone to touch engine directly
                4. Inheritance - Reuse
                👉 Electric car uses features of normal car
     - type() to check the type of object something is eg print(type([]))
     - class 
             - User defined objects are created using the class keyword. The class is a blueprint that defines the nature of a future object.
             - From classes we can construct instances. An instance is a specific object created from a particular class.
                     - # Create a new object type called Sample
                     class Sample:
                         pass 
                     # Instance of Sample
                     x = Sample() 
                     print(type(x))
             - we give classes a name that starts with a capital letter.
     - Attribute
             - An attribute is a characteristic of an object. A method is an operation we can perform with the object.
             - syntax for creating an attribute is: self.attribute = something
             - There is a special method called: __init__()  used to initialize the attributes of an object
                     class Dog:
                        def __init__(self,breed):     #This is METHOD.  this breed is used below after equal, both should be same as both are same variable
                            self.breed = breed
                     sam = Dog(breed='Lab')
                     frank = Dog(breed='Huskie')
             -__init__ is a setup function. It runs automatically when you create an object. Think of it as “object birth process"
             - The special method __init__() is called automatically right after the object has been created.
     - Class object attributes
             - These Class Object Attributes are the same for any instance of the class.
             - Class Object Attribute is defined outside of any methods in the class
                     class Dog:
                     # Class Object Attribute
                     species = 'mammal'
                     def __init__(self,breed,name):
                        self.breed = breed
                        self.name = name
     - Methods 
             - Methods are functions defined inside the body of a class
             - They are used to perform operations with the attributes of our objects.
     - Inheritance
             - Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes.
             - Important benefits of inheritance are code reuse and reduction of complexity of a program. The derived classes (descendants) override or extend the functionality of base classes.
     - Polymorphism
             - polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in.
     -  abstract classes
             - An abstract class is one that never expects to be instantiated.
     - special methods
             - __init__(), __str__(), __len__() and __del__() methods
             - They allow us to use Python specific functions on objects created through our class

21. Modules
     - Modules in Python are simply Python files with the .py extension, which implement a set of functions
     - Modules are imported from other modules 
     - import math
     - Two very important functions come in handy when exploring modules in Python - the dir and help functions
22. Packages
     - Packages are name-spaces which contain multiple packages and modules themselves
     - Library
        └── Package
            └── Module
                └── Class
                        └── Method / Function

23. Errors and Exception Handling
     -  to handle errors in Python we have try and except statements.
                     -  try:
                        You do your operations here...
                        ...
                        except ExceptionI:
                        If there is ExceptionI, then execute this block.
                        except ExceptionII:
                        If there is ExceptionII, then execute this block.
                        ...
                        else:
                        If there is no exception then execute this block.
     - We can also just check for any exception with just using except:
     - try executes main block, if it fails, it goes to except block
     - finally The finally: block of code will always be run regardless if there was an exception in the try code block.
                     - def askint():
                        while True:
                            try:
                                val = int(input("Please enter an integer: "))
                            except:
                                print("Looks like you did not enter an integer!")
                                continue
                            else:
                                print("Yep that's an integer!")
                                print(val)
                                break
                            finally:
                                print("Finally, I executed!")
24. Unit Testing
     - Equally important as writing good code is writing good tests. Better to find bugs yourself than have them reported to you by end users!
     - These are simple tools that merely look at your code, and they'll tell you if there are style issues or simple problems like variable names being called before assignment.
     - pylint
             - pylint tests for style as well as some very basic program logic. you should install pylint.
     - unittest
             - unittest lets you write your own test programs. The goal is to send a specific set of data to your program, and analyze the returned results against an expected result.

26. Decorators
     - Decorators provide a way to modify functions using other functions.They help to make your code shorter and more "Pythonic".
     - Remember that in Python everything is an object. That means functions are objects which can be assigned labels and passed into other functions. 
     - Even though we deleted the name hello, the name greet still points to our original function object. It is important to know that functions are objects that can be passed to other objects. If a function greet is there which is pointing to function hello, and we delete hello still greet will work.
     - A function which is defined under another function is called a nested function. This nested function cannot be called outside the main function.it can only be called inside that particular function.
     - when you put a pair of parentheses after it, the function gets executed; whereas if you don’t put parentheses after it, then it can be passed around and can be assigned to other variables without executing it.
                        def new_decorator(func):

                            def wrap_func():
                                print("Code would be here, before executing the func")

                                func()

                                print("Code here will execute after the func()")

                            return wrap_func
                        @new_decorator
                        def new_fun():
                            print("This function is in need of a Decorator")
                        new_fun()

27. Iterators and Generators
     - Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off. 
     - allowing us to generate a sequence of values over time. 
     -  they don't actually return a value and then exit. Instead, generator functions will automatically suspend and resume their execution and state around the last point of value generation
     - The main advantage here is that instead of having to compute an entire series of values up front, the generator computes one value and then suspends its activity awaiting the next instruction. This feature is known as state suspension. 
     - yield > Pauses function , Produces many values, Function resumes, Generator function
                         def gencubes(n):
                            for num in range(n):
                                yield num**3
                         for x in gencubes(10):
                            print(x)
     - If we use empty list and append it for every loop it will also work, but by doing this all values will be stored in memory. For small data its ok, but for large dataset this will create issue. So Generator and yield are used in those cases.
     - Next() - next() function allows us to access the next element in a sequence. 
                         def simple_gen():
                            for x in range(3):
                                yield x
                                 
                         g = simple_gen()
                         print(next(g))  # 0
                         print(next(g))	 # 1
         - After yielding all the values next() caused a StopIteration error. What this error informs us of is that all the values have been yielded.
     - Iter() -  a string object supports iteration, but we can not directly iterate over it as we could with a generator function. The iter() function allows us to do just that!. its used for string.
                         s = 'hello'
                         s_iter = iter(s)
                         print(next(s_iter))
                 


28. Advanced Python modules
     - Counter  - Counter is a dict subclass which helps count hashable objects. Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.
             - from collections import Counter
             lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
             Counter(lst)   # Counter({1: 6, 2: 6, 3: 4, 12: 1, 21: 1, 32: 1, 223: 1})
                sum(c.values())                 # total of all counts
                c.clear()                       # reset all counts
                list(c)                         # list unique elements
                set(c)                          # convert to a set
                dict(c)                         # convert to a regular dictionary
                c.items()                       # convert to a list of (elem, cnt) pairs
                Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
                c.most_common()[:-n-1:-1]       # n least common elements
                c += Counter()                  # remove zero and negative counts
     
29. Opening and Reading Files
     - pwd -- gives the directory where the notebook is actually stored.
     - os -- built-in os module that allows us to use operating system dependent functionality
     - os.getcwd() --  gives the directory where the notebook is actually stored.
     - os.listdir() -- returns a list containing the names of the entries in the directory given by path
     - Moving Files  shutil - to move files to different locations. Keep in mind, there are permission restrictions, for example if you are logged in a User A, you
                     won't be able to make changes to the top level Users folder without the proper permissions
                             import shutil
                             shutil.move('practice.txt','\\Users\\Marcial') #moves to marcial folder
                             shutil.move('\\Users\\Marcial\practice.txt',os.getcwd()) # moves to current directory
     - Deleting Files - 3 methods for deleting files:
                     1.os.unlink(path) which deletes a file at the path your provide
                     2.os.rmdir(path) which deletes a folder (folder must be empty) at the path your provide
                     3.shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path.
                     All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin instead of permanent removal.
                             pip install send2trash
                             import send2trash
                             send2trash.send2trash('practice.txt')
                    
30. datetime module
     - deal with timestamps in your code
     - Time values are represented with the time class. Times have attributes for hour, minute, second, and microsecond. They can also include time zone information
                             import datetime
                             t = datetime.time(4, 20, 1)
                             print(t)
                             print('hour  :', t.hour)
                             print('minute:', t.minute)
                             print('second:', t.second)
                             print('microsecond:', t.microsecond)
                             print('tzinfo:', t.tzinfo)
    
                             today = datetime.date.today()
                             print('ctime:', today.ctime())
                             print('tuple:', today.timetuple())
                             print('ordinal:', today.toordinal())
                             print('Year :', today.year)
                             print('Month:', today.month)
                             print('Day  :', today.day)
                             print(today)

                             print('Earliest  :', datetime.time.min)
                             print('Latest    :', datetime.time.max)
                             print('Resolution:', datetime.time.resolution)                            
                             print('Earliest  :', datetime.date.min)
                             print('Latest    :', datetime.date.max)
                             print('Resolution:', datetime.date.resolution)
   
31. Math and Random Modules
                             import math
                             math.floor(value)  #4.35 to 4
                             math.ceil(value)   #4.35 to 5
                             round(value)  #4.35 to 4 , nearest even value it will roundup, bankers rule
                             math.pi
                             math.sin(10)

                             import random
                             random.randint(0,100) # 1 random number between 0 to 100
                             mylist = list(range(0,20))  # 0 to 19 
                             random.choice(mylist)  # random from that list
                             random.choices(population=mylist,k=10)  # with replacement , same number can be multiple times
                             random.sample(population=mylist,k=10) # no duplicates
                             random.shuffle(mylist)

32. Python Debugger
     - You've probably used a variety of print statements to try to find errors in your code. A better way of doing this is by using Python's built-in debugger module (pdb). 
     -  It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, so you can understand what your program actually does and find bugs in the logic.

33. Regular Expressions
     - sometimes called regex for short allows a user to search for strings using almost any sort of rule they can come up.
                             import re
                             text = "The person's phone number is 408-555-1234. Call soon!"
                             pattern = 'phone'
                             match = re.search(pattern,text) # if not found none is returned
                             match.span()  # gives index positions of the macthes
                             match.start()
                             match.end()
                             matches = re.findall("phone",text)   # find all phone in text multiple values
                             for match in re.finditer("phone",text):
                                 print(match.span())  # To get actual match objects, use the iterator:
     - Patterns
                             phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
                             patttern to search in the strings
         Character	Description	    Example Pattern Code	Exammple Match
            \d	    A digit 	        file_\d\d	            file_25
            \w	    Alphanumeric	    \w-\w\w\w              	A-b_1
            \s	    White space     	a\sb\sc	                a b c
            \D	    A non digit     	\D\D\D	                ABC
            \W	    Non-alphanumeric    \W\W\W\W\W	            *-+=)
            \S	    Non-whitespace	    \S\S\S\S	            Yoyo


         Character	Description	            Example Pattern Code	Exammple Match
            +	    Occurs one or more times	Version                 \w-\w+	Version A-b1_1
            {3}	    Occurs exactly 3 times  	\D{3}	                abc
            {2,4}	Occurs 2 to 4 times     	\d{2,4}	                123
            {3,}	Occurs 3 or more	        \w{3,}	                anycharacters
            \*	    Occurs zero or more times	A\*B\*C*	            AAACC
            ?	    Once or none	            plurals?	            plural


                             re.search(r'\d{3}-\d{3}-\d{4}',text)
                             phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
                             phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # complie is like formula set for search pattern
                             results = re.search(phone_pattern,text)
                             results.group()   # creates a group of all matched values
                             results.group(1)  # shows 1 value from the group
                             re.search(r"man|woman","This woman was here.")  # search man or woman in string and give output
                             re.findall(r'\d$','This ends with a number 2')   # $ is used to find ending with
                             re.findall(r'^\d','1 is the loneliest number.') # ^ is used to find starting with
                            
34. Timing your code
     - Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project. Python has a built-in timing module to do this.
     - We can try using the time module to simply calculate the elapsed time for the code. Keep in mind, due to the time module's precision, the code needs to take at least 0.1 seconds to complete.
                             # STEP 1: Get start time
                             start_time = time.time()
                             # Step 2: Run your code you want to time
                             result = func_one(1000000)
                             # Step 3: Calculate total time elapsed
                             end_time = time.time() - start_time
     - Timeit Module
         - What if we have two blocks of code that are quite fast, the difference from the time.time() method may not be enough to tell which is fater. In this case, we can use the timeit module.
         - The timeit module takes in two strings, a statement (stmt) and a setup. It then runs the setup code and runs the stmt code some n number of times and reports back average length of time it took.
                             timeit.timeit(stmt2,setup2,number=100000)
            
35. Unzipping and Zipping Files
     - The zipfile library is built in to Python, we can use it to compress folders or files. To compress all files in a folder, just use the os.walk() method to iterate this process for all the files in a directory.
     - Create Zip file first , then write to it (the write step compresses the files.)
                             comp_file = zipfile.ZipFile('comp_file.zip','w')
                              #creates file  
                             f = open("new_file2.txt",'w+')
                             f.write("Here is some text")
                             f.close()
                             # creates zip file then add other files to it
                             import zipfile
                             comp_file = zipfile.ZipFile('comp_file.zip','w')  # created a zip folder
                             comp_file.write("new_file2.txt",compress_type=zipfile.ZIP_DEFLATED)   # new_file2 is placed in the zip folder
                             comp_file.close()
     - Unzipping file
         - We can easily extract files with either the extractall() method to get all the files, or just using the extract() method to only grab individual files. 
                             zip_obj = zipfile.ZipFile('comp_file.zip','r')
                             zip_obj.extractall("extracted_content")  
                             # single file extraction
                             zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
                             zip_obj.extract('data/file1.csv', 'extracted_content')
                             zip_obj.close()
     - Often you don't want to extract or archive individual files from a .zip, but instead archive everything at once. The shutil library that is built in
     - The shutil library can accept a format parameter, format is the archive format: one of "zip", "tar", "gztar", "bztar", or "xztar".
                             import shutil , os
                             directory_to_zip = '/Volumes/pyspark_python/pyspark/ext_vol' # this directory all file folders will be zip
                             output_filename = 'example'  # in current directory the zip will be created , not avaialble in volume of unity catalog directly
                             shutil.make_archive(output_filename,'zip',directory_to_zip)
                             os.path.exists(directory_to_zip)   # checks if we have access to path or not
                             # below command is for extracting any compressed folers file, just give extension like zip
                             shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')

36. Working with CSV
     - import csv
     - Encoding - Often csv files may contain characters that you can't interpret with standard python, this could be something like an @ symbol, or even foreign characters
                             import csv
                             data = open('example.csv')
                             data
                             csv_data = csv.reader(data)
                             data_lines = list(csv_data)
                             
                             data = open('example.csv',encoding="utf-8")
                             csv_data = csv.reader(data)
                             data_lines = list(csv_data)
                             
                             data_lines[:3]
                             
                             all_emails = []
                             for line in data_lines[1:15]:
                                 all_emails.append(line[3])                      
     - Writing to new CSV Files 
                             file_to_output = open('to_save_file.csv','w',newline='')
                             csv_writer = csv.writer(file_to_output,delimiter=',')
                             csv_writer.writerow(['a','b','c'])
                             csv_writer.writerows([['1','2','3'],['4','5','6']])
                             file_to_output.close()
     - Existing File
                             f = open('to_save_file.csv','a',newline='')
                             csv_writer = csv.writer(f)
                             csv_writer.writerow(['new','new','new'])
                             f.close()
37. Overview of Sending Emails
     - The smtplib library allows you to manually go through the steps of creating and sending an email in Python.
     - Create an SMTP object for a server. Here are the main Server Domain Name for the top email services
     - Next is to create an STMP object that can make the method calls to log you in to your email in order to send messages. 
     - Next we run the ehlo() command which "greets" the server and establishes the connection. This method call should be done directly after creating the object. Calling it after other methods may result in errors in connecting later on. The first item in the tuple that is returned should be 250, indicating a successful connection.
     - When using the 587 port, this means you are using TLS encryption, which you need to initiate by running the starttls() command. If you are using port 465, this means you are using SSL and you can skip this step.
     - Now its time to set up the email and the passwords. You should never save the raw string of your password or email in a script, because anyone that sees this script will then be able to see you email and password! Instead you should use input() to get that information. If you also don't want your password to be visible when typing it in, you can use the built-in getpass library that will hide your password as you type it in, either with asterisks or by just keeping it invisible.

38. With Statement
     - When you open a file using f = open('test.txt'), the file stays open until you specifically call f.close(). Should an exception be raised while working with the file, it remains open. This can lead to vulnerabilities in your code, and inefficient use of resources.
     - Open the file → use it → automatically close it.  Even if an error happens.
                                 with open("data.csv", "w") as f:
                                 f.write("id,name\n")
                                 f.write("1,Alice\n")


                             




                            



                            



























