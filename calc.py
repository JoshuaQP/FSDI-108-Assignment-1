""" Script: simple Calculator
    Author: Joshua Palmier 
     Year: 2021 
     Functionality: Basic mathematical operations  """


#imports


#global


#functions

def print_menu():
    print("_" *30)
    print(" PyCalc")
    print("_" * 25)
 
    print("[1] -Sum")
    print("[2] -Subtract")
    print("[3] -Multiplication")
    print("[4] -Division")
    print("[5] -Is it even? ")
    print("[q] -Quit")

#instructions

selected_option = ""
while(selected_option != "q"):
    print_menu()
    selected_option = input("please select an option: ")
    if(selected_option == 'q'):
        break
    
    
    if (selected_option == "5"):
        num5 = float(input("Pick me any number:"))
        result = num5 % 2
        results = result == 0

    elif(results == 0  ):
        print("Even number")
    

        break
  
    num1 = float(input("provide num 1 :"))
    num2 = float(input("provide num 2 :"))
    

    if(num1 / num2 == '0'):
     print("choose an diffrent number!!")

    if (selected_option == "1"):
        
        result =(num1) + (num2)
        print(result) 

    elif (selected_option =="2"):
    
        result = (num1) - (num2)
        print(result)

    elif (selected_option =="3"):
    
        result = (num1) * (num2)
        print(result)

    elif (selected_option =="4"):
         if(num2 == 0):
             print("**Error: Division by zero is not allowed")
             break

print("Good bye!")
    
"""


ask for two numbers 
sum the numbers 
print the result

"""
