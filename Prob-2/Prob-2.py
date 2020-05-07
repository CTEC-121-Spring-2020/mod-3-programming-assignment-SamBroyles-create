# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Sam Broyles

'''
Input:  employee's name
        hourly wage
        hours worked
Process:   calculate overtime wage
            total week pay
            taxes to be taken out
            medical to be taken out
            final pay after taxes
Output: employee name
        base hourly wage
        overtime wage
        tax withholding
        medical insurance withholding
        total take home pay
'''

def main():
    #get employee info
    print()
    employeeName = input("What is your name?\n ")
    employeePay = input("What is your hourly wage?\n ")
    employeeHours = input("How many hours have you worked?\n ")

    #calculate employee overtime
    if float(employeeHours) > 40:
        (employeeOTpay) = float(employeePay) * 1.5
    else:
        employeePay == employeePay
    
    #employees total pay
    employeeTotal = float(employeePay) * float(employeeHours)
    #taxes and medical
    employeeTax = float(employeeTotal) * .2
    employeeMedical = float(employeeTotal) * .1
    employeeTotal = float(employeeTotal) - float(employeeTax) - float(employeeMedical)
    
    #final output of employee info and pay
    print("\nEmployee Name:", employeeName)
    print("\nRegular Wage:", employeePay)
    if float(employeeHours) <= 40:
        print("\nOvertime Wage: none")
    else:
        print("\nOvertime Wage:", float(employeeOTpay))
    print("\nTotal Tax Withholding:", employeeTax)
    print("\nTotal Medical Withholding:", employeeMedical)
    print("\nTotal Take Home Pay:", employeeTotal)
    print()

main()