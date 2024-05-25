import sys

"""
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arg")
"""

#check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is" , sys.argv[1])


#sys.exit
if len(sys.argv) < 2:
    sys.exit("Too few")


print("Hello, my name is" , sys.argv[1])


#name tags for everyone
if len(sys.argv) < 2:
    sys.exit("Too Few MF")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)