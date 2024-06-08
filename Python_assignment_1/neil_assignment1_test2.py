#write a program to read 2 integer m and n & swap there value with or without using a temperary variable
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
 m = m + n  
 n = m - n
 m = m - n
 print ("The Value of m after swapping using temp variable: ",m)
 print ("The Value of n after swapping using temp variable: ",n)

m = int(input("enter a value of m :"))
n = int(input("enter a value of n :"))
with_swap(m,n)
without_swap(m,n)