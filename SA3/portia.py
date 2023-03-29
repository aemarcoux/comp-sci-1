# Author: Alexander Marcoux
# Date: 17 January 2023
# Purpose: calculating and comparing interest on an invest made 2021 years ago

BRUTUS_INTEREST = 1.05
PORTIA_INTEREST = 1.04
BRUTUS_PRINCIPLE = 1.00
PORTIA_PRINCIPLE = 100000
portia_value = 100000
brutus_value = 1.00
year = 0
CURRENT = 2021

while brutus_value <= portia_value:
    portia_value = portia_value * PORTIA_INTEREST
    brutus_value = brutus_value * BRUTUS_INTEREST
    year = year + 1
print("The year is " + str(year) + ". Brutus' balance is " + str(brutus_value) + ", and Portia's balance is " + str(portia_value))

