"""
Student: Sameer Ahadi
Course: CSC-101
Date: 11/09/2025
Description: Income tax calculator
"""


def calc_AGI(wages, interest, unemployment):
    
    return abs(wages) + abs(interest) + abs(unemployment)

def get_deduction(status):
    
    if status == 0:
        return 6000
    elif status == 1:
        return 12000
    elif status == 2:
        return 24000
    else:
        return 6000

def calc_taxable(agi, deduction):
    # taxable and deduction, but not less than 0
    t = agi - deduction
    if t < 0:
        t = 0
    return t

def calc_tax(status, taxable):
    # round the final tax
    tax = 0.0
    if status == 2:
        # Married
        if taxable <= 20000:
            tax = 0.10 * taxable
        elif taxable <= 80000:
            tax = 2000 + 0.12 * (taxable - 20000)
        else:
            tax = 9200 + 0.22 * (taxable - 80000)
    else:
        # Dependent/Single
        if taxable <= 10000:
            tax = 0.10 * taxable
        elif taxable <= 40000:
            tax = 1000 + 0.12 * (taxable - 10000)
        elif taxable <= 85000:
            tax = 4600 + 0.22 * (taxable - 40000)
        else:
            tax = 14500 + 0.24 * (taxable - 85000)
    return round(tax)

def calc_tax_due(tax, withheld):
    # if withheld < 0, treat it as 0
    if withheld < 0:
        withheld = 0
    return tax - withheld

def main():
    # Step 1: inputs (integers)
    wages = int(input("Enter wages (integer): "))
    interest = int(input("Enter taxable interest (integer): "))
    unemployment = int(input("Enter unemployment compensation (integer): "))
    status = int(input("Enter filing status (0-Dependent, 1-Single, 2-Married): "))
    withheld = int(input("Enter taxes withheld (integer): "))

    # Steps 2-6: calculations
    agi = calc_AGI(wages, interest, unemployment)
    deduction = get_deduction(status)
    taxable = calc_taxable(agi, deduction)
    tax = calc_tax(status, taxable)
    tax_due = calc_tax_due(tax, withheld)

    # output
    print()
    print("AGI:", agi)
    print("Deduction:", deduction)
    print("Taxable income:", taxable)
    print("Tax:", tax)
    print("Withheld:", 0 if withheld < 0 else withheld)
    print("Tax due:", tax_due)

if __name__ == "__main__":
    main()
