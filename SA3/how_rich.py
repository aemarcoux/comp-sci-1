# Author: Alexander Marcoux
# Date: 17 January 2023
# Purpose: calculating interest on an invest made 2021 years ago
# general form n(year number) = 1.00(1.05)^n

PRINCIPLE = 1.00
INTEREST = 1.05
value = 1.00
year = 0
CURRENT = 2021

while year <= CURRENT:
    print("At year " + str(year) + ", the balance is " + str(value))
    value = value * INTEREST
    year = year + 1



