# wap to find sum of even number which are divisible by 2 ,3 ,5 up to 'n' number where n is entered by user.
n = int(input("Enter a number: "))
s = 0
for i in range(30, n+1, 30):
 s += i
print("Sum of even numbers divisible by 2, 3, and 5 up to", n, "is:", s)