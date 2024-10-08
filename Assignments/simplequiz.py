#string functions
#string functions are a group of functions that modify string
#they manipulate them
# .Lower()
# .Lower() changes the string to be all lowercase
# .upper() changes the string to uppercase
# .capitalize() changes the entire string to lowercase, then capitalizes the first letter
# .title() changes the entire string to title case
# "Hello World"
# .swapcase () inverts the capitalization of each character, "Hello World > hELLO wORLD"

x = "Lord of the rings" 
x = x.lower()
print(x)

question_one = input("What year did Michael Jackson die?\n")
question_two = input("Who is the Queen of Rap?\n")
question_three = input("Who is better than Michael Jackson\n")
question_four = input("Which pasta is the best?\n")
question_five = input("Which west african country is the best?\n")



def tally_score():
    score = 0
    if question_one == "2009":
        score = score + 1
    if question_two == "Nicki Minaj":
        score = score + 1
    if question_three == "Nobody":
        score = score + 1
    if question_four  == "Chicken alfredo":
        score = score + 1
    if question_five == "LIBERIA":
        score = score + 1
    print(str(score) + "/5")

tally_score()
