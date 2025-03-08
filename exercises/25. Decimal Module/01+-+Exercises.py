import csv
from time import perf_counter
from decimal import Decimal
import decimal

# ### Question 1

# There is a file named `transactions.csv` which is a list of purchases and sales.
# Write code that loads this data and calculates the total of these purchases and sales.
# Take two approaches - one using floats, and one using Decimal objects.
# Calculate the difference between the two results.
# Also, time how long it takes to run your code using floats and using Decimals.

# Read the first few lines of the file to understand the structure
with open('transactions.csv') as f:
    for _ in range(8):
        print(next(f).strip())

# Function to calculate the total sum using either float or Decimal
def total_sum(file_name, *, dec=False):
    sum_total = 0
    with open(file_name) as f:
        reader = csv.reader(f)
        next(f)  # Skip the header

        for row in reader:
            amount = row[-1]

            if dec:
                sum_total += Decimal(amount)
            else:
                sum_total += float(amount)

    return sum_total

trans = './transactions.csv'

# Time the process for Decimal
start = perf_counter()
print(f'Decimal: {total_sum(trans, dec=True)}')
# Uncomment the line below to print the float result
# print(f'Float: {total_sum(trans)}')
end = perf_counter()
elapsed = end - start
print(f'Elapsed: {elapsed}')

# Function to calculate the total sum using float only
def total_sum_float(file_name):
    amounts = []
    with open(file_name) as f:
        reader = csv.reader(f)
        next(f)  # Skip the header

        for row in reader:
            amounts.append(float(row[-1]))

    return sum(amounts)

# Time the process for Float
start = perf_counter()
print(f'Total: {total_sum_float(trans)}')
end = perf_counter()
elapsed = end - start
print(f'Elapsed: {elapsed}')

# ### Question 2

# Using the same file (`transactions.csv`), we now want to calculate a fee on each transaction.
# Irrespective of whether the transaction was a credit or a debit, we will calculate a `0.123%` transaction fee for the (absolute) values of each transaction.
# Each fee calculation precision should be limited to `8` digits after the decimal point (so use `round(val, 8)`)
# In addition, any rounding should always round ties away from `0` (`ROUND_HALF_UP`) - and not use Banker's rounding (`ROUND_HALF_EVEN`).
# Only implement this solution using `Decimal` objects, as floats do not offer a rounding algorithm choice, and writing our own rounding algorithm can be overly complicated.
# Also calculate the difference in the fee totals when using `ROUND_HALF_UP` vs `ROUND_HALF_EVEN`.

def fee_sum(file_name, *, fee='0.00123', round_meth=decimal.ROUND_HALF_UP, digits=8):
    with decimal.localcontext() as ctx:
        ctx.rounding = round_meth

        fee = Decimal(fee)
        total = 0

        with open(file_name) as f:
            reader = csv.reader(f)
            next(f)  # Skip the header

            for row in reader:
                amount = row[-1]
                amount = Decimal(amount)
                fee_val = round(abs(fee * amount), digits)
                total += fee_val

        return total

file = './transactions.csv'

# Calculate the fee sum using ROUND_HALF_UP
half_up = fee_sum(file, round_meth=decimal.ROUND_HALF_UP)
# Calculate the fee sum using ROUND_HALF_EVEN (Banker's rounding)
half_even = fee_sum(file, round_meth=decimal.ROUND_HALF_EVEN)

# Calculate the difference between the two rounding methods
difference = half_up - half_even
print(f'Difference between ROUND_HALF_UP and ROUND_HALF_EVEN: {difference}')
