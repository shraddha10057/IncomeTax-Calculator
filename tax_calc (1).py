print("--- Simple Income Tax Calculator  ---")
try:
    gross_income = float(input("Enter Gross Annual Income: "))
    deductions = float(input("Enter Deductions (Standard Deduction is usually 75000): "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

taxable_income = gross_income - deductions

if taxable_income < 0:
    taxable_income = 0
print("\nTaxable Income: " + str(taxable_income))

tax = 0

if taxable_income <= 300000:
    tax = 0

elif taxable_income <= 700000:
    tax = (taxable_income - 300000) * 0.05

elif taxable_income <= 1000000:
    tax = 20000 + (taxable_income - 700000) * 0.10

elif taxable_income <= 1200000:
    tax = 50000 + (taxable_income - 1000000) * 0.15

elif taxable_income <= 1500000:
    tax = 80000 + (taxable_income - 1200000) * 0.20

else:
    tax = 140000 + (taxable_income - 1500000) * 0.30

if taxable_income <= 700000:
    tax = 0

cess = tax * 0.04
total_tax = tax + cess

print("-" * 30)
print(f"Base Tax:      {tax:.2f}")
print(f"Cess (4%):     {cess:.2f}")
print("-" * 30)
print(f"Total Payable: {total_tax:.2f}")
print("-" * 30)