# Lesson 3: This program says hello and asks for my name

print("Hello world")

# ask for their name
print("What is your name?") 
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))

# ask for their age
print("WHat is your age?") 
myAge = input()
print("You will be " + str(int(myAge) + 1) + ' in a year.')

# You cannot concatinate a string and an in together
# You cannot add a string to an int