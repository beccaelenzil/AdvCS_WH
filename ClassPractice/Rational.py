import math

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

    def simplify(self):
        done = True
        output = 1
        minimum = min(self.numerator, self.denominator)
        for num in range(minimum,1,-1):
            output = num
            if (self.numerator%num == 0) and (self.denominator%num==0):
                break
        return Rational(self.numerator/output,self.denominator/output)

r1 = Rational(1,2)
r2 = Rational(1,3)
r3 = r1 + r2
r4 = Rational(5,6)
r5 = Rational(10,20)
r6 = Rational(100,50)
r7 = Rational(1,6)
print r1 == r2
print r3 == r4
print r3
print r5.simplify()
print r6.simplify()
print r7.simplify()