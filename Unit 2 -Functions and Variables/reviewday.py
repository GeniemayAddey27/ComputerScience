# 2 basic functions
# You know something is a function because it has () at the end
# The stuff that goes in those () are called parameters
# parameters are information that the function needs to run
# "I say jump, you say how high" "How high" is the parameter
print("Hello World!") # "Hello World" is the parameter
input("What is your favorite animal?\n")
# \n is called an escape chracter (linebreak)
# input is never required, only use it when necessary

# Variables
# Variables are a way to store data for later use in the program
# Syntax (grammar)
# name = value
x = 5 # x is the variable name, 5 is the value
# Snake naming convention - sall lowercase, underscores for spaces
# CONSISE: Short and descriptive
username = "Osowski"               # Define string (string of characters)
fav_animal = "Lemur"               # Define string 
total_poptarts = 12                # Define integer   (whole numbers)
percent_complete = 23.52           # Define float      (Decimal numbers)
is_cool = True                     # define Boolean    (true/false values)
first_letter = 'c'                 # define character  (single keyboard symbol)

total_poptars = 8                  #reassigning variable

# Arithmetic operators (sounds scary, just basic math)
#  t - / * ** % //
print(2 + 2)
print("2" + "2")

my_variable = 2 + 3

# Working programs
# add two numbers using input
x = input("What is x?") # input function always returns a string
y = input("What is y?\n>")  
print(int(x)+ int(y))  # convert string into int and print result

#2. Converrt Celcius to F
temp_celcius = 49
temp_f = (temp_celcius * 1.8) + 32
print(temp_f)

# Conversion functions
str()
int()
float()
bool()
bin()

# Functions, are a lot like variables and can be recalled from memory by calling their namw
# stores infornamtion
# store code
# def name ():
def potato():
    print("tomato")
potato() # Every function call needs parenthesis, even with n parameters


def jump(how_high):
    print("You jumped " + how_high + " inches high.")

jump(14)
# scope
# Global vs local variables
#Gloabal: defines at no indentation level
#Local: defines inside of functions, also parameters are local variables
#Gloabl variables can be ua=sed anywhere
todd  = "cool guy" #Global varibale - no indentation level

# Local variables only exist in the context the y were defined in
# return functions
# Functions can also return values
# The value that is returned is sent back to where the function was called
#The function does its work, and returns an answer back

def add_two_numbers(x,y):
    print(x + y)
    return(x + y)

print(add_two_numbers(10, 5))


