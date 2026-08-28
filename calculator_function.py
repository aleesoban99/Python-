num1=int(input("what is first number:"))
num2=int(input("what is second number:"))
operator=input("what is operator:")
def solve(num1,num2,operator):
    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
    else:
        print("some error occured")
solve(num1,num2,operator)