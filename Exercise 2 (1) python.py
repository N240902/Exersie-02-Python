 # Question 1: Arithmetic and Assignment Operators
x=9
y=3
# TODO: Add 3 to x using the += operator
x+=3
# TODO: Multiply y by 2 using the *= operator
y*=2
# TODO: Divide x by y and store the result in a variable called 'result'
result=x/y
# TODO: Print the value of 'result'
print(result) 
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a=8
b=5
c=9
# TODO: Create a condition that checks if a is greater than b
print(a>5)

# TODO: Create a condition that checks if b is even (hint use the modulus operator)
modulus=(b%2)
print(modulus ==0)
#    TODO: Create a condition that checks if c is less than or equal to a
print(c<=a)
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

#  TODO: Print the value of 'final_condition'
print(a>b or b%2)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score
score=int(input("enter a score :"))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score>=90:
    print("A")
elif score>=79:
    print("B")
elif score>=69:
    print("C")
elif score>=59:
    print("D")
else :
    print("F")

# TODO: Print the grade for the given score
    print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1=int(input("enter a num1"))
num2=int(input("enter a num2"))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation=input("Please select from the following: +, -, *, /")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
results=0
if operation=="+":
    print= num1 + num2
    print(result)
 
elif operation=="-":
    print(result)
elif operation=="*":
    print(result)
elif operation=="/":
    print(result)
else :
    print(result)

# TODO: Handle the case of division by zero
if num2==0 :
    
# TODO: Print the result of the operation
    print("ayou cannot devide by zero/0r")


def withdraw(amount):
     balance =1000
     if balance<amount :
        print("don't have enough funds")
        return
        currentAmount =balance-amount
        print("you have R(currentAmount) left in youraccount")
        withdraw(withdraw)