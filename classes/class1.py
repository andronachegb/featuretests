class Test:
    def __init__(self, number):
        self.number = number

    def is_odd(self):
        if self.number % 2 == 0:
            return "is odd"
        else:
            return "is not odd"

    def factorial(self):
        result = 1
        for i in range(1, self.number+1):
            result *= i

        return result