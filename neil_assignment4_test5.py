# convert integer into binary number
def int_to_binary(number):
    return bin(number).replace('0b', '')
a =int(input("enter a integer number :"))
b = int_to_binary(a)
print(f"The binary representation of {a} is: {b}")
c = int(input("enter a negative number :"))
binary_number_negative = int_to_binary(c)
print(f"The binary representation of {c} is: {binary_number_negative}")