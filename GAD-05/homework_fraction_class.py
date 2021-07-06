class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            print("Denominator of a fraction can not be 0.")
            raise ZeroDivisionError

    def __str__(self):
        return f"{int(self.numerator)}/{int(self.denominator)}"

    def __add__(self, other):
        result_nominator = self.numerator * other.denominator + self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator

        return Fraction(result_nominator / self.greatest_common_divisor(result_nominator, result_denominator),
                        result_denominator / self.greatest_common_divisor(result_nominator, result_denominator))

    def __sub__(self, other):
        result_nominator = self.numerator * other.denominator - self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator

        return Fraction(result_nominator / self.greatest_common_divisor(result_nominator, result_denominator),
                        result_denominator / self.greatest_common_divisor(result_nominator, result_denominator))

    @staticmethod
    def greatest_common_divisor(a, b):
        while b != 0:
            (a, b) = (b, a % b)
        return a

    def inverse(self):
        auxiliary = self.numerator
        self.numerator = self.denominator
        self.denominator = auxiliary
        return Fraction(self.numerator, self.denominator)


fraction_1 = Fraction(1, 5)
fraction_2 = Fraction(4, 9)
fraction_3 = Fraction(7, 6)

print(fraction_1 + fraction_2 - fraction_3.inverse())
