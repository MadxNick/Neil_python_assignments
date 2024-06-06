# ramesh basic salary is input through keyboard . his dearness allowance is 40% of basic salary and house rent allowance is 20% his basic salary. write a program to calculate his gross salary
basicsalary =float(input("enter the basic salary salary of ramesh :"))
dearnessallowance = (40*100/basicsalary)
houserent = (20*100/basicsalary)
grosssalary = (basicsalary+dearnessallowance+houserent )
print(dearnessallowance)
print(houserent)
print(basicsalary)
print(grosssalary)
