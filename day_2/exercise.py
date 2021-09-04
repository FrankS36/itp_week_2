# ITP Week 2 Day 2 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers

a =1
b = 2
c = 3
d = 4

def subtract():
  print(a - b)
subtract()

def product():
  print(a * b * c)
product()
  
def sum():
  print(a + b + c + d)
sum()


# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string) to all the user to add, substract, multiply and divide.

def do_math():
    print("choose an operation")
    op = input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Divide")
    a = float(input("First number"))
    b = float(input("Second number"))
    if op == 1: 
        print(a + b)
    elif op == 2:
        print(a - b)
    elif op == 3:
        print(a * b)
    else:
        print(a // b)
do_math()

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.
def split_tab():
    total_bill = float(input("What is the total bill amount? "))
    tip = float(input("What percentage tip would you like to leave? "))
    num_ppl = int(input("How many people are in your party? "))
    pmt_person = (total_bill * ( 1 + float(tip/100)))/num_ppl
    print("Each person must pay: ", pmt_person)
split_tab()

