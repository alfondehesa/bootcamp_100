
def prime_checker(number):

    count = number - 1
    prime = "It's a prime number."

    while count>1:
        if number % count == 0:
            prime = "It's not a prime number."
        count -= 1
    print(prime)




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
