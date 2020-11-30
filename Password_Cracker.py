# Example Of Cracking Password Using Python:
# Cracking A Numeric Password Using Python:
import random
password = random.randrange(9213) # set any amount of password length inside random range function
print("The Random Password Is: {}".format(password))
print("Cracking the password now !")
x = 0 # first value of x 
if (x == password): # optional code
    print("Password Found: {}".format(x)) # optional code 
while (x != password):
    for x in range(0,1000000000000000000000000000000000000000000000): 
            if (x == password):
                print("Password found !")
                print("Password = {}".format(x))
                break
            else:
                print("Trying password: {}".format(x))
