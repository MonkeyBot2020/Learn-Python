#This is a comment. The python interpreter runs your code line by line, and checks for any errors.
'''This is a multi-line comment. You can't use these beside lines of code, but you can use #'''
#Python is best on Visual Studio Code. Enable the integrated terminal using {Control + `} on Mac.
#And remember - I'm using Python 3, not 2 as provided by default on the Mac!

#Just a little code to make counting and organizing easy! Find out about this further down. 
x = 0
def counter():
  global x
  x = x+1
  return x

'''VARIABLES AND CONDITIONAL OPERATORS'''

#This is how you store and print from variables.
print("\n" + str(counter()) + ". VARIABLES IN PYTHON")
print("This is how to write appostrophies ' - see how easy it is when you enclose it between quotes?")
my_variable = "Hello world!" #Stores a string variable. 
my_bool = True
print("This is a string: " + my_variable + "; This is a boolean: " + str(my_bool) + "; This is a variable: " + str(10*34)) #You can't concatenate strings and non-strings together, you have to convert the non-string into a string using the str() method. 

#Some math operations.
print("\n" + str(counter()) + ". MATH OPERATORS")
print(10**2) #This means 10^2.
print(3%2) #Modulo returns the remainder from a division. So, if you type 3 % 2, it will return 1, because 2 goes into 3 evenly once, with 1 left over.

#In Python, whitespace is used to structure code. Whitespace is important, so you have to be careful with how you use it. We will use two-space indentation (two blank spaces for each indentation) to make sure you can easily read code with multiple indentations in your browser. 

#Access by Index - each character in a string is assigned a number. This number is called the index.
print("\n" + str(counter()) + ". STRINGS & CONSOLE OUTPUT")
print("This is first letter of CATS, we start counting the index from 0 instead of 1: " + "cats"[0] + "; Third letter of DOG: " + "dog"[2])
print("Use len() to calculate length of a string 'foobar': " + str(len("foobar")))
print("Use 'STRING'.lower() OR my_variable.lower() method to remove capitalization in strings: " + 'STRING'.lower())
print("Use 'string'.upper() OR my_variable.upper() method to capitilize the string: " + 'string'.upper())
print("Use str(2) to turn non-strings into strings: " + str(2))
print("String formatting using %s - " + "The %s who %s %s!" % ("Knights", "say", "Ni")) #This will print "The Knights who say Ni!"

#Methods that use dot notation (such as 'String'.upper() or 'String'.lower()) only work with strings. On the other hand, len(string) and str(object) can work on other data types.

#Conditional statements.
#The following the_random_function() returns True.
def the_random_function():
    if 3==3 and 2<3 and 3<=3 and 3!=4 or 5>4 or 5>=4:
      print("\n5. CONDITIONAL STATEMENTS") #Start coding here!
      print("the_random_function() is - True.")
        #Don't forget to indent the code inside this block!
    elif not 2>3:
      print("This is false")
    else:
      print("The end")
        #You'll have to call the_random_function() to execute it.
the_random_function()

'''BUILT-IN FUNCTIONS AND IMPORTING FUNCTIONS'''

#Python's built-in functions (BIF)
print("\n" + str(counter()) + ".BUILT IN FUNCTIONS")
dir(__builtins__)

#Importing methods from the datetime library.
from datetime import datetime #Import module 'datetime' from library 'datetime'.
print("\n" + str(counter()) + ". DATE & TIME LIBRARY")
print("Print the current date & time: " + str(datetime.now()))
print("Print the current dd/mm/year: %s/%s/%s" % (datetime.now().day, datetime.now().month, datetime.now().year))

#Importing functions from modules.
import math #Generic import of the MATH module.
print(math.sqrt(25)) #This tells Python not only to import math, but to get the sqrt() function from within math.
everything = dir(math) #Sets everything to a list of things from math
print(everything) #Prints 'em all!

from math import sqrt
print(sqrt(25)) #It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it's done with the from keyword.

from math import * #Universal import statement to import all functions.
print(max(2,5,18)) #The max() function takes any number of arguments and returns the largest one. 
print(min(2,4,61)) #Returns the smallest of a given series of arguments.
print(abs(-42)) #Returns the absolute value of the number it takes as an argument.
print(type(42)) #Returns the type of the data it receives as an argument.

'''CREATING NEW FUNCTIONS'''

#Defining new functions.
def distance_from_zero(s):
  if type(s) == int or type(s) == float:
    return abs(s)
  else:
    return('Nope')
print(distance_from_zero(-42))

'''LISTS, NESTED LISTS, FOR AND WHILE LOOPS (AND BREAK STATEMENTS)'''

#Python lists.
print("\n" + str(counter()) + ". LISTS")
letters = ['a', 'b', 'c']
the_list = ['a', 'b', 'c',[1,2,3,['k','l','m']]] #You can create a list within a list!
string_list = "Hello world!" #A list can even be a string!
letters.append('d') #Appends an additional element to the end of the list.
splice = letters[0:3] #Takes a subsection and store it in the slice list. We start at the index before the colon and continue up to but not including the index after the colon.
letters.insert(2, 'z') #Inserts the letter 'z' into position 2 in the list.
print(len(letters))
print(letters)
print(the_list)
letters[:2] #Grabs the first two items.
letters[3:] #Grabs the fourth through last items.
print(letters.index('c')) #Print the first index that contains the string 'c'.

#"for" and "while" loops.
print("\n" + str(counter()) + ". 'FOR' AND 'WHILE' LOOPS (AND BREAK STATEMENTS)")
for each_letter in letters: #Easy way to iterate printing a list, insetad of typing 'print' statements for each variable!
  print(each_letter)

count = 0 #When you use "while" loops, you have to worry about state information which requires you to employ a counter variable. This gives you additional unnecessary work!
while count < len(letters):
  print(letters[count])
  count = count+1

#Simple "for" loop. This is simpler than the above "while" loop.
for x in range(3):
  print("This is item: " + str(x)) #Remember - x begins with 0, hence range(3) will print 0, 1, 2.

#This while loop checks if the 'name' variable matches the given string.
name = ''                           # (1)
while name != 'your name':          # (2)
    print('Please type your name.')
    name = input()                  # (3)
print('Thank you!')

#There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains the break keyword.
while True:                         # (1)
    print('Please type your name.')
    name = input()                  # (2)
    if name == 'your name':         # (3)
        break                       # (4)
print('Thank you!')    

#Printing loops within loops. Note that the "for" loop will prints the outer loop ONLY. The inner list is printed "as-is."
print(the_list)
for element in the_list:
  print(element)

#isinstance() conditional statement to check if a data object is of some specified type.
print("\n" + str(counter()) + ". CONDITIONAL STATEMENTS")
for element in the_list:
  if isinstance(element, list): #Checks to see if the element is a nested list.
    for nested in element:
      print(nested)
  else:
    print(element)

'''RECURSIVE FUNCTIONS'''

#Recursion of functions. 
print("\n" + str(counter()) + ". RECURSION OF FUNCTIONS (FUNCTIONS THAT CALL THEMSELVES)")
def recursive_function(the_list):
  for each_item in the_list:
    if isinstance(each_item, list): #Checks to see if the element is a nested list.
      print(recursive_function(each_item)) #The function calls itself.
    else:
      print(each_item)
recursive_function(the_list)

'''STRING MANIPULATION'''

string_list = "Hello world!" #A list can even be a string!

#String manipulation.
print("\n" + str(counter()) + ". STRING MANIPULATION")
string_list[:string_list.find(" ")] #Finds the empty space within the string, truncates it and returns only the word "Hello".

