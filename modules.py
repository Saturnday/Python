"""
    -sys.argv, json
    -how to import modules
    -how to exit a program
"""

#
import sys
if len(sys.argv)>2:
    sys.exit("to many args")
elif len(sys.argv)<2:
    sys.exit("too few args")
print("Hello"+ sys.argv[1])
