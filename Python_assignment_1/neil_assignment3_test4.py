 # write a program to check whether the triangle is valid or not
a = float(input("Enter side A of the triangle: "))
b = float(input("Enter side B of the triangle: "))
c = float(input("Enter side C of the triangle: "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("The triangle is valid.")
        else:
         print("The triangle is invalid.")
    else:
        print("The triangle is invalid.")
else:
    print("The triangle is invalid.")