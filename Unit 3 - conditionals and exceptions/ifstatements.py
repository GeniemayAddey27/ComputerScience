# IF statements evaluate boolean expressions
# they make decisions about whihc code to run next

# Take a temperature
# Print "<temperature> is hot" if its >= 80
# Otherwise, print "<temperature is not hot"
temp = input("Whats the temperature in F\n>")
temp = int(temp)

#if <boolean expression> :
# should remind of writing a function
# def <name> ():

if temp >= 80:
    print(str(temp)) + " is hot!"

else: #otherwise
    print(str(temp) + " is not hot:")

#not all if statements need an else, none of them need an else
# Else statements are an option, they are optional
# All else statements must have a corresponding if statement
# Else statements cannot exist alone
# AN if statement can only have one else


#Create a program that asks for a password
# If the password is correct, print ACCESS GRANTED
#Other wise, print ACCESS DENIED
# The password is skibidi68.9

password = input("Insert password\n>")
if password  == 
