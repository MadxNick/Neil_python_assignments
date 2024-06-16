# wap to check enter int number is palidrome or not .
integer = int(input("Enter an integer: "))
if str(integer) == str(integer)[::-1]:
    print(f"{integer} is a palindrome.")
else:
    print(f"{integer} is not a palindrome.")
