# ramesh basic salary is input through keyboard . his dearness allowance is 40% of basic salary and house rent allowance is 20% his basic salary. write a program to calculate his gross salary
basicsalary =float(input("enter the basic salary salary of ramesh :"))
dearnessallowance = (40*100/basicsalary)
houserent = (20*100/basicsalary)
grosssalary = (basicsalary+dearnessallowance+houserent )
print(dearnessallowance)
print(houserent)
print(basicsalary)
print(grosssalary)


# Checked but formula applied is incorrect
# marks obtained 1/5 
# Below is corrected code

basicsalary = float(input("Enter the basic salary of Ramesh: "))
# Calculate dearness allowance which is 40% of basic salary
dearnessallowance = 0.4 * basicsalary # 40 * basicsalary / 100
# Calculate house rent allowance which is 20% of basic salary
houserent = 0.2 * basicsalary
# Calculate gross salary
grosssalary = basicsalary + dearnessallowance + houserent

# Output the results
print(f"Dearness Allowance: {dearnessallowance}")
print(f"House Rent Allowance: {houserent}")
print(f"Basic Salary: {basicsalary}")
print(f"Gross Salary: {grosssalary}")
