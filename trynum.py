# Written by : Mohak
# Date : 29/12/2023
# Time : 2:00AM
# Notepad Ref 3.1 : Write a python Program which writes 1 to 6 in horizontal line with 6 spaces as well as their square as well as their square root upto 2 decimal places.

for i in range(1,7):
    print(i,end="      ")
print()

for i in range(1,7):
    print(i**2,end="      ")
print()

for i in range(1,7):
    print(round(i**0.5,2),end="      ")
print()
