# if a 5 digit no is input through the keyboard write a program to calculate the sum of its digits
def getSum(n):
  sumr = 0
  while (n != 0):
    sumr += (n % 10)
   # print(sumr)
    n = int(n/10)
  return sumr
n = float(input("Enter the 5 digit no : "))
print(getSum(n))