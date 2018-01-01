#This is a comment. The python interpreter runs your code line by line, and checks for any errors.
'''This is a multi-line comment. You can't use these beside lines of code, but you can use #'''
'''Python is best on Visual Studio Code. Enable the integrated terminal using {Control + `} on Mac'''

'''This is how you store and print from variables.'''
print "\n1. VARIABLES IN PYTHON"
my_variable = "Hello world!" #Stores a string variable. 
my_bool = True
print "This is a string: " + my_variable + "; This is a boolean: " + str(my_bool) + "; This is a variable: " + str(10*34) #You can't concatenate strings and boolean together, hence you need to change boolean to string variable using the str() method. 

'''Some math operations'''
print "\n2. MATH OPERATORS"
print 10**2 #This means 10^2.
print 3%2 #Modulo returns the remainder from a division. So, if you type 3 % 2, it will return 1, because 2 goes into 3 evenly once, with 1 left over.

'''In Python, whitespace is used to structure code. Whitespace is important, so you have to be careful with how you use it. We will use two-space indentation (two blank spaces for each indentation) to make sure you can easily read code with multiple indentations in your browser. '''