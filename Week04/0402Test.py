#What are the two functions of sys module and their usage? 
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arg")
else:
    for i in sys.argv[1:]:
        print("Hello, " + i)
        