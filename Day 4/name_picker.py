# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# This program will pick a random name from a list.

for i in range(0,len(names)):

    names[i] = names[i].replace(" ","")

index=random.randint(0,len(names)-1)

print(names[index] + ' is going to buy the meal today!')



