"""
a. Define a function arithmetic_operation() which takes 2 numbers and operation name as input and performs an ope
ration on them:
* opname: "Add" - Then we add 2 numbers
* opname: "Sub" - Then we subtract 2 numbers
* opname: "Multiply" - Then we multiply 2 numbers
* opname: "Divide" - Then we divide the 2 numbers
Print the result of the operation and also return it.
"""
def arithmetic_operation(a,b,op_name) :
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
    print(result)
    return result

arithmetic_operation(22,7,"Divide")

