Module-1  Basics
1. Numbers
     - Integers = 2,-3
     - Floating = 2.5 , 4E2(4x10^2)

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
     - String functions called Methods var.upper(), var.split(),  var.startswith() , var.endswith() 
     - isupper() , islower() , isnumeric() , isalpha() , isalnum()
     - Indendation 4 spaces per indendation
4. Lists
     - can store different datatype []
     - Lists are mutable
     - List indexing , slicing , concate(+) , List methods , nested list
     - List comprehension - creates a NEW list by looping over an iterable and collecting value
     - .append() , .extend() , .insert() , .remove() , .pop() , .clear() , .index() , .count() , .sort() , .reverse()
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
     - Booleans (with predefined True and False displays that are basically just the integers 1 and 0). It also has a placeholder object called None.
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



Module-2 Python statements
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
    - enumerate - enumerate() walks through a list and gives you two things at the same time:
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
                        def __init__(self,breed):       # this breed is used below after equal, both should be same as both are same variable
                            self.breed = breed
                     sam = Dog(breed='Lab')
                     frank = Dog(breed='Huskie')
             -__init__ is a setup function. It runs automatically when you create an object. Think of it as “object birth process"
             - The special method __init__() is called automatically right after the object has been created.
     
            
               
    
                

   

























