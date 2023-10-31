#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ran = number * -1
    ran = ran % 10
    ran = ran * -1
else:
    ran = number % 10
print ("Last digit of {}".format(number), end=' ')
if ran > 5:
    print("is {} and is greater than 5".format(ran))
elif ran == 0:
    print("is {} and is 0".format(ran))
elif ran < 6 and num != 0:
    print("is {} and is less than 6 and not 0".format(ran))
