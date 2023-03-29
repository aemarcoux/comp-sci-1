# Author: Alexander Marcoux
# Date: 11 Feb 2023
# Purpose: creating a counter driver
from counter import Counter

# counter with a limit of 60 and a starting value of 0, meaning it should wrap back up to lim - 1
counter1 = Counter(60, 0, 4)
# counter with a limit of 60 and starting value of 15
counter2 = Counter(60, 15, 4)

# proving that the boolean value returns true when wrapped
c1 = counter1.tick()
print(c1)

# printing the value it wrapped to: lim - 1
print(counter1.get_value())
print(str(counter1))

# showing that when the len of value is less than min digits, the str is padded to the left with zeros
print(str(counter2))
counter2.tick()
print(str(counter2))
counter2.tick()
print(str(counter2))
