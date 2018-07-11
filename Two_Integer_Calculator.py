###########################################################################
# Author: Brittny Woods
# Course: CMST290, Spring 2016
#
#
# Program Name: Project 3, Two Integer Calculator
# Due Date: February 29, 2016 at 12:01 AM
#
# Programming Language Used:  Python 3
#
# Program information:
#    This program calculates any two numbers given
###########################################################################

def print_mainmenuoptions( ):
    print("Main Menu Options:")
    print(" 'H' for Main Menu")
    print(" 'A' for Addition")
    print(" 'S' for Subtraction")
    print(" 'M' for Multiplication")
    print(" 'D' for Division")
    print(" 'I' for Integer Division")
    print(" 'E' to exit the program")

def addition(add1, add2):
    return add1 + add2

def subtraction(sub1, sub2):
    return sub1 - sub2

def multiplication(mul1, mul2):
    return mul1 * mul2

def division(div1, div2):
    return div1 / div2

def integer_division(int_div1, int_div2):
    return int_div1 // int_div2

choice = "H"
while choice != "E":
    if choice == "A":
        print("**This function finds the SUM of TWO numbers**")
        add1 = float(input("Enter first number: "))
        add2 = float(input("Enter second number: "))
        print("Total =", addition(add1, add2))
        choice = input("choose function: ")
    elif choice == "S":
        print("**This function finds the DIFFERENCE of TWO numbers**")
        sub1 = float(input("Enter first number: "))
        sub2 = float(input("Enter second number: "))
        print("Total =", subtraction(sub1, sub2))
        choice = input("choose function: ")
    elif choice == "M":
        print("**This function finds the PRODUCT of TWO numbers**")
        mul1 = float(input("Enter first number: "))
        mul2 = float(input("Enter second number: "))
        print("Total =", multiplication(mul1, mul2))
        choice = input("choose function: ")
    elif choice == "D":
        print("**This function finds the QUOTIENT of TWO numbers**")
        div1 = float(input("Enter first number: "))
        div2 = float(input("Enter second number: "))
        print("Total =", division(div1, div2))
        choice = input("choose function: ")
    elif choice == "I":
        print("**This function finds the QUOTIENT of TWO integers**")
        int_div1 = float(input("Enter first integer: "))
        int_div2 = float(input("Enter second integer: "))
        print("Total =", integer_division(int_div1, int_div2))
        choice = input("choose function: ")
    elif choice == "H": 
        print_mainmenuoptions( )
        choice = input("choose function: ")
