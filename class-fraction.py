class Fraction(object):
    """ a number representation as a fraction"""

    def __init__(self, num, denum):
        """ num and denum are integrers """
        assert type(num) == int and type(denum) == int, "ints not used"
        self.num = num
        self.denum = denum

    def __str__(self):
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denum)

    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denum + self.denum*other.num
        bott = self.denum*other.denum
        return Fraction(top, bott)

    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denum - self.denum*other.num
        bott = self.denum*other.denum
        return Fraction(top, bott)

    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denum

    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denum, self.num)


f = Fraction(2.0, 3)
