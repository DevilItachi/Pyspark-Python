Module-1  Basics
1. Numbers
    Integers = 2,-3
    Floating = 2.5 , 4E2(4x10^2)

2. Variable assignments
    - dont use l,o,I as variable names as this are confusing
3. Strings
    - single, double , triple quotes to write strings. Double mostly preffered.
    - String indexing , slicing , concate(+) , String functions called Methods(var.upper(), .split(), etc.)
    - f Strings {} = inserts strings in strings 
4. Lists
    - can store different datatype []
    - Lists are mutable
    - List indexing , slicing , concate(+) , List methods , nested list
    - List comprehension - creates a NEW list by looping over an iterable and collecting value
5. Dictionaries
    - key value pairs {}
    - can store different datatype 
    - Dictionaries are mutable
    - Dictionary indexing , slicing , concate(+) , Methods , nested Dictionary
    - .keys(), .values() , .items() , sorted(d.values())
6. Tuples
    - immutable , but similar to List ()
    - If want to modify tuple, convert to list perform operation, convert back to tuple
7. Sets and booleans
    - Sets are an unordered collection of unique elements () . The result of set is in {}
    - List can be converted to set, which will not have duplicates, and again converted back to list
    - Booleans (with predefined True and False displays that are basically just the integers 1 and 0). It also has a placeholder object called None.
8. Comparison operators
    - output a Boolean value (True or False).
    - == , != , > , <,  >= ,  <=
    - And , Or 
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
                --------------------------------------------------------------
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
                    print('x is currently: ',x)
                    print(' x is still less than 10, adding 1 to x')
                    x+=1
                    if x==3:
                        print('Breaking because x==3')
                        break
                    else:
                        print('continuing...')
                        continue
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
    - input - takes input from the user, cluster keeps running until user enters something
                - input('Enter Something into this box: ')

12. List Comphrension
    - allow us to build out lists using a different notation. You can think of it as essentially a one line for loop built inside of brackets
                mylist = [x for x in range(0,11)]
                

   

























