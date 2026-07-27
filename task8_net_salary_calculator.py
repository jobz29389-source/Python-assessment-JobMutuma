"""Task 8: Net-Salary Calculator"""

# a. Employee details
payroll_no = "PN001"
name = "Job Mutuma"
gender = "Male"
department = "IT"
basic_salary = 40000

# b. Gross pay
house_allowance = 6500
medical_allowance = 5500
gross_pay = basic_salary + house_allowance + medical_allowance

# c. PAYE
if gross_pay <= 20000:
    paye_rate = 0.00
elif gross_pay <= 30000:
    paye_rate = 0.04
elif gross_pay <= 40000:
    paye_rate = 0.05
else:
    paye_rate = 0.06
paye = gross_pay * paye_rate

# d. NHIF & NSSF
nhif = gross_pay * 0.02
nssf = basic_salary * 0.03

# e. Deductions & net pay
total_deductions = paye + nhif + nssf
net_pay = gross_pay - total_deductions

# f. Display
print("=" * 40)
print(f"Payroll No: {payroll_no}")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Department: {department}")
print("-" * 40)
print(f"Basic Salary: Ksh {basic_salary:,.2f}")
print(f"Gross Pay: Ksh {gross_pay:,.2f}")
print(f"PAYE: Ksh {paye:,.2f}")
print(f"NHIF: Ksh {nhif:,.2f}")
print(f"NSSF: Ksh {nssf:,.2f}")
print(f"Total Deductions: Ksh {total_deductions:,.2f}")
print(f"Net Pay: Ksh {net_pay:,.2f}")
print("=" * 40)