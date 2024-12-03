class Rectangle:

    def __init__(self, width, height=None):
        self.width = width
        self.height = height
        

    @property
    def width(self):
        if not self.__width:
            return("--no width--")
        return self.__width
    
    @width.setter
    def width(self, value):
        try:
            if(self.__width):
                print("Width can't be changed")
            else:
                self.__width=value
        except:
            self.__width=value
    @width.deleter
    def width(self):
        raise AttributeError("Width can't be deleted")
            
            
        
    @property
    def height(self):
        if not self.__height:
            return("--no height--")
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if(self.__height):
                print("You can't height")
            else:
                self.__height=value
        except:
            self.__height=value   
    @height.deleter
    def height(self):
        raise AttributeError("Height can't be deleted")
    
    def area(self):
        if (isinstance(self.height, int|float) and isinstance(self.width, int|float)):
            area = self.height*self.width
        else:
            area=None
        return area
    def __str__(self):
        return f"{self.width} x {self.height} = {self.area()}"


x = Rectangle(10, None)
print(x)
x.width = 15
x.height=16
print(x)