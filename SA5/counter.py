# Author: Alexander Marcoux
# Date: 11 Feb 2023
# Purpose: creating a Counter class

class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        self.value = initial
        self.digits = min_digits

        # informing the user that the initial value is outside of the counter's limit
        if self.value > self.limit - 1 or self.value < 0:
            print("Value is outside the parameters of the counter; the new value is", str(self.limit - 1))
            self.value = self.limit - 1

    def get_value(self):
        return self.value

    def __str__(self):
        # returning the value as a string and padding to the left wit zeros to meet the min digits
        if len(str(self.value)) < self.digits:
            x = self.digits - len(str(self.value))
            return str('0' * x) + str(self.value)

        return str(self.value)

    def tick(self):
        self.value = int(self.value) - 1

        # returning a boolean if the value is wrapped back to lim - 1
        if self.value < 0:
            self.value = self.limit - 1
            return True
        return False