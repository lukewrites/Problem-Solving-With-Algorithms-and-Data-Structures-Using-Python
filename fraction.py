def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def common(num, denom):
    return gcd(num, denom)

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, newden//common)

    def __div__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __lt__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return (new_num > )

    def __gt__(self, other):
        pass

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x * y)
print(x / y)
