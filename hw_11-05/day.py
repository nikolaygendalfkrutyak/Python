class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y=y
        self.r=r
        
    def __mul__(self, other):
        self.r*=other

    def __floordiv__(self, other):
        self.r//=other
    def __gt__(self, other):
        return self.r > other.r
    def __ge__(self, other):
        return self.r>= other.r   
    def __lt__(self, other):
        return self.r < other.r
    def __le__(self, other):
        return self.r<= other.r  
    def __eq__(self, other):
        return self.r == other.r
    def __ne__(self, other):
        return self.r!= other.r  
circle_1 = Circle (1, 2, 3)
circle_2 = Circle(2, 3, 4)
print( circle_1>circle_2)