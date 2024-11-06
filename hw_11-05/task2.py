import math
class Proper_Fraction():
    def __init__(self, a, b, whole =0):
        self.k = whole
        self.a=a
        self.b=b
        self.__reduce()
        
    def __reduce(self):
        self.k+=self.a//self.b
        self.a-=self.b*(self.a//self.b)
        if (self.a<0):
            self.a+=self.b
            k-=1
        k = math.gcd(self.a, self.b)
        self.a//=k
        self.b//=k
    def __iadd__(self, other):
        if isinstance (other, Proper_Fraction):
            self.k+= other.k
            self.a=self.a*other.b+self.b*other.a
            self.b*=other.b
            self.__reduce()
            return self
        return NotImplemented
    
    def __add__(self, other):
        k=self.k + other.k
        a=self.a*other.b+self.b*other.a
        b=self.b *other.b
        return Proper_Fraction(a, b, k)
    def __sub__(self, other):
        k=self.k - other.k
        a=self.a*other.b-self.b*other.a
        b=self.b *other.b
        return Proper_Fraction(a, b, k)
    def __isub__(self, other):
        if isinstance (other, Proper_Fraction):
            self.k-= other.k
            self.a=self.a*other.b-self.b*other.a
            self.b*=other.b
            self.__reduce()
            return self
        return NotImplemented
    def __imul__(self, other):
        a=(self.k*self.b+self.a)*(other.k*other.b+other.a) 
        b=self.b*other.b
        return Proper_Fraction(a, b)
    def __mul__(self, other):
        self.a=(self.k*self.b+self.a)*(other.k*other.b+other.a)
        self.b*=other.b
        self.__reduce()
        return self
    
    def __str__(self):
        if self.k and self.k!=-1:        
            return (f"{self.k} whole and {self.a}/{self.b}  or {self.k*self.b+self.a}/{self.b}")
        else:
            return (f"{self.k*self.b+self.a}/{self.b}")
    def __lt__(self, other):
        return (self.k + self.a/self.b) < (other.k + other.a/other.b)

    def __gt__(self, other):
        return (self.k + self.a/self.b) > (other.k + other.a/other.b)

    def __le__(self, other):
        return (self.k + self.a/self.b) <= (other.k + other.a/other.b)

    def __ge__(self, other):
        return (self.k + self.a/self.b) >= (other.k + other.a/other.b)

    def __eq__(self, other):
        return (self.k + self.a/self.b) == (other.k + other.a/other.b)

    def __ne__(self, other):
        return (self.k + self.a/self.b) != (other.k + other.a/other.b)
fr1 = Proper_Fraction(7, 11)
fr2 = Proper_Fraction(23, 17)
fr3 = Proper_Fraction(14, 17)
fr4=fr2-fr3
print(fr1>fr2)
print (fr1>fr4)
fr1+=fr3
print(fr1)
print (fr1>fr2)
print(fr3>fr2)
print(fr3-fr1)
