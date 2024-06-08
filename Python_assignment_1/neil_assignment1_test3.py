# ramesh basic salary is input through keyboard . his dearness allowance is 40% of basic salary and house rent allowance is 20% his basic salary. write a program to calculate his gross salary
basicsalary = float(input("Enter the basic salary of Ramesh: "))
dearnessallowance = 0.4 * basicsalary
houserent = 0.2 * basicsalary
grosssalary = basicsalary + dearnessallowance + houserent
print(f"Dearness Allowance: {dearnessallowance}")
print(f"House Rent Allowance: {houserent}")
print(f"Basic Salary: {basicsalary}")
print(f"Gross Salary: {grosssalary}")