print("|  Welcome to Calculator App  |")

num1 = input("first Number : ")
num2 = input("Second Number : ")

int_num1 = float(num1)
int_num2 = float(num2)

adding = int_num1 + int_num2
subtract = int_num1 - int_num2
multiply = int_num1 * int_num2
divide = int_num1 / int_num2
modulus = int_num1 % int_num2

print("|  ----------------------------  |")

print("Adding :", adding)
print("subtract:", subtract)
print("multiply:", multiply)
print("divide:", divide)
print("modulus:", modulus)
