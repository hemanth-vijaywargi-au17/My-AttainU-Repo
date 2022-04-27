"""
b. Redefine the same function with default values for numbers as 3 and 5 and opname as "Add". Use the same function
 to calculate 5+3-12+23
"""

def arithmetic_operation(a=3,b=5,op_name="Add"):
    if op_name=="Add":
        result=a+b
    elif op_name=="Sub":
        result=a-b
    elif op_name=="Multiply":
        result=a*b
    elif op_name=="Divide":
        result=a/b
    else:
        print("Invalid Input")
    return result

x = arithmetic_operation(5,3,"Add")
y = arithmetic_operation(-12,23,"Add")
print( x + y )
