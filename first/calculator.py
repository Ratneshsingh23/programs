def add(a, n):
    return a+n
def sub(a, n):
    return a-n
def mul(a, n):
    return a*n
def div(a, n):
    if n==0:
        return "invalid"
    return a/n
print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice = input("enetr you opertaion")
try:
    num1 = int(input("enetr first num"))
    num2 = int(input("enetr second num"))

    if choice == "1":
        print("result",add(num1, num2))
    elif choice == "2":
        print("result", sub(num1, num2))
    elif choice == "3":
        print("result", mul(num1, num2))
    elif choice == 4:
        print("result", div(num1, num2))
    else:
        print("you have slected wrong number")
except Error:
    print("invalid input")