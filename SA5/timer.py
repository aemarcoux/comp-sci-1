# Author: Alexander Marcoux
# Date: 11 February 2023
# Purpose: creating a timer class
from counter import Counter


class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    def __str__(self):
        if len(str(self.hours)) < self.hours.digits:
            x = self.hours.digits - len(str(self.hours))
            self.hours = str('0' * x) + str(self.hours)

        elif len(str(self.minutes)) < self.minutes.digits:
            x = self.minutes.digits - len(str(self.minutes))
            self.minutes = str('0' * x) + str(self.minutes)

        elif len(str(self.seconds)) < self.seconds.digits:
            x = self.seconds.digits - len(str(self.seconds))
            self.seconds = str('0' * x) + str(self.seconds)

        # returning the values in the form hours:minutes:seconds and padding the value with 0s to reach min digits
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def tick(self):
        # wrapping the values once they reach zero and prompting the other values to start ticking
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()

    def is_zero(self):
        # returning boolean when the timer reaches 00:00:00
        if self.hours.value == 0 and self.minutes.value == 0 and self.seconds.value == 0:
            return True
        return False

