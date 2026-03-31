# IncomeTax-Calculator
 Python-based command-line tool to calculate income tax based on gross annual income and deductions. This script determines the taxable income, applies specific tax slabs, and calculates the final payable tax including a 4% cess.

## Features
* **Interactive Input**: Prompts the user for Gross Annual Income and Deductions.
* **Automatic Deductions Calculation**: Computes taxable income by subtracting deductions from gross income.
* **Tax Slab Logic**: Applies progressive tax rates based on income brackets:
    * **0 - 3,00,000**: Nil
    * **3,00,001 - 7,00,000**: 5%
    * **7,00,001 - 10,00,000**: 10% (+ fixed base)
    * **10,00,001 - 12,00,000**: 15% (+ fixed base)
    * **12,00,001 - 15,00,000**: 20% (+ fixed base)
    * **Above 15,00,000**: 30% (+ fixed base)
* **Rebate Support**: Tax is reduced to zero if taxable income is ₹7,00,000 or less.
* **Cess Calculation**: Adds a 4% Health and Education Cess to the base tax.


## How to Run
1.  Clone the repository or download the `tax_calc.py` file.
2.  Open a terminal or command prompt.
3.  Navigate to the directory containing the file.
4.  Run the script using the following command:
    

