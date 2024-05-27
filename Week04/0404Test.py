#How to create own modules?
import sys 
from TestModule import hello
from TestModule import goodbye

if len(sys.argv) != 2:
    sys.exit("Too few argv")

else: 
    hello(sys.argv[1])
    goodbye(sys.argv[1])