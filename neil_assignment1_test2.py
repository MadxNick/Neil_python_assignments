#write a program to read 2 integer m and n & swap there value with or without using a temperary variable
def swap () :
 print("hello")
m = (input("enter a value of m :"))
n = (input("enter a value of n :"))
temp = m
m = n
n = temp
print ("The Value of m after swapping: ",m)
print ("The Value of n after swapping: ",n)

# Marks 1/5
# Checked read the question properly it has been written with and without using any temp variable
# and function's use is not done properly correct code is below:
def with_swap(m,n):
 print ("The Value of m before swapping using temp variable: ",m)
 print ("The Value of n before swapping using temp variable: ",n)
 temp = m
 m = n
 n = temp
 print ("The Value of m after swapping using temp variable: ",m)
 print ("The Value of n after swapping using temp variable: ",n)

def without_swap(m,n):
 print ("The Value of m before swapping using temp variable: ",m)
 print ("The Value of n before swapping using temp variable: ",n)
 m = m + n  # also can be written as m+=n
 n = m - n
 m = m - n  # also can be written as m-=n
 print ("The Value of m after swapping using temp variable: ",m)
 print ("The Value of n after swapping using temp variable: ",n)

with_swap(m,n)
without_swap(m,n)
