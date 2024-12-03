class Bank_Account:

    def __init__(self, name, ballance=None):
        self.name = name
        self.__ballance = ballance

    @property
    def ballance(self):
        if not self.__ballance:
            return("no attribute")
        return self.__ballance

    @ballance.setter
    def ballance(self, ballance):
        if not isinstance(ballance, int | float|None):
            raise TypeError("Ballance must be a number")
        if ballance!=None and ballance <= 0 :
            raise ValueError("Ballance must be greater than 0")
        self.__ballance = ballance
        
    def __str__(self):
        return f"{self.name} - {self.ballance}"
    @ballance.deleter
    def ballance(self):
        self.ballance=None

    
x = Bank_Account("sjh0110", 10)
print(x.name)
print(x)
print(x.ballance)
del(x.ballance)
print(x.ballance)
x.name = "sdfjj003"
print(x)