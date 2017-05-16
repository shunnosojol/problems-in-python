#https://www.hackerrank.com/challenges/30-conditional-statements
#!/bin/python3

import sys


n = int(input().strip())
if n>=6 and n<=20:
    print("Weird")
elif n==4:
    print("Not Weird")
elif n%2==1:
    print("Weird")
elif n%2==0:
    print("Not Weird")
else:
   print("Not Weird")