class User:

    def __init__(self, first_name, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        if not self.__first_name:
            return("--no first name--")
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        try:
            if(self.__first_name):
                print("You can't set first name")
            else:
                self.__first_name=value
        except:
            self.__first_name=value
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Names can't be deleted")
            
            
        
    @property
    def last_name(self):
        if not self.__last_name:
            return("--no last name--")
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        try:
            if(self.__last_name):
                print("You can't set last name")
            else:
                self.__last_name=value
        except:
            self.__last_name=value   
    @last_name.deleter
    def last_name(self):
        raise AttributeError("Names can't be deleted")
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


x = User("Apple")
print(x)
x.first_name = "sdfjjsn"
x.last_name="good"
print(x)