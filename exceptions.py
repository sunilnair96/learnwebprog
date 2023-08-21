import sys
try:
    x = int(input(" X :"))
    y = int(input(" Y :"))
except ValueError:
    print ("Enter number only")
    sys.exit(1)
try:
    result = x / y
except ZeroDivisionError:
    print ("cannot divide by 0")
    sys.exit(1)
print (f"{x} divided by {y} is  {result}")