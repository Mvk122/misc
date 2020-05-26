class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom

    def simplify(self):
        # simplifies a fraction with the highest common factor of the numerator and denominator
        highest = 0
        for i in range(self.denom):
            if self.denom % (i + 1) ==0:
                if self.num % (i + 1) == 0:
                    if i + 1 > highest:
                        highest = i + 1
        num = int(self.num / highest)
        denom = int(self.denom / highest)
        return Fraction(num, denom) 

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        first = self.num * other.denom
        second = other.num * self.denom
        denominator = self.denom * other.denom
        return Fraction(first + second, denominator).simplify()

    def __sub__(self, other):
        first = self.num * other.denom
        second = other.num * self.denom
        denominator = self.denom * other.denom
        return Fraction(first - second, denominator).simplify()

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom).simplify()

    def __truediv__(self, other):
        return Fraction(self.num* other.denom, self.denom* other.num).simplify()

    def __float__(self):
        return self.num / self.denom 
