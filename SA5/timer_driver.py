# Author: Alexander Marcoux
# Date: 12 February 2023
# Purpose: creating a timer driver
from timer import Timer

start = Timer(1, 30, 0)
# print the starting value
print(str(start))

# print timer until 00:00:00
while start.is_zero() == False:
    start.tick()
    print(str(start))
