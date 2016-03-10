class Rational:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def __repr__(self):
        val = str(self.numerator) + "/" + str(self.denominator)
        return val

    def __add__(self, other):
        newNumerator = self.numerator * other.denominator + self.denominator * other.numerator
        newDenominaor = self.denominator * other.denominator
        return Rational(newNumerator, newDenominaor)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __ne__(self, other):
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __str__(self):
        val = str(self.numerator) + "/" + str(self.denominator)
        return val



r1 = Rational(1,2)
r2 = Rational(1,3)
r3 = r1 + r2
r4 = Rational(5,6)
print r1 == r2
print r3 == r4
print r3
