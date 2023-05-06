#
# Copyright Isaac Libby 2023
#
# BSD Licence
#


import sys
import math
import numpy

# print(sys.argv[1])
# :print(sys.argv[2])


if (len(sys.argv) < 3) or (len(sys.argv) > 3):
    print ("usage: python basic_structures [-h | -g] [name]")
    quit() 


opt = sys.argv[1]
person = sys.argv[2]


def greeting(greetingType):
    i = 0
    while i< 12:
        i = i + 1
        print (greetingType + ", " + person + "! (" + str(i) + ")" )

# Main Code
if opt == '-h':
    greeting('Hello')
elif opt == '-g':
    greeting('Goodbye')

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print((index + 1), fruit)

# math
print("Math Time")
theNumber = 8.5332532;
print(math.ceil(theNumber))
print(math.pi)

# Standard deviation example 
a = numpy.array([1, 2, 3, 4])
print(numpy.std(a))

