from calc import *
'''
Here we are importing the function which are present in another file.
Now that file has been imported as a module, so we can use the functions which are present in that file or module.

'''

m=int(input("Enter a number: "))
n=int(input("Enter a number: "))

print(f"Addition = {add(m,n)}")
print(f"Subtraction = {subt(m,n)}")
print(f"Multiplication = {mult(m,n)}")
print(f"Division = {divd(m,n)}")
