class Date:
    def __init__(self, day=10, month=11, year=2024):
        if not (isinstance(day, int) and isinstance(month, int) and isinstance (year, int)):
            raise TypeError("Thats not a date")
        self.dates={
            "January" : 31,
            "February" : 28, 
            "March" : 31,
            "April" : 30,
            "May" : 31, 
            "June" :30,
            "July" : 31,
            "August" : 31,
            "September" : 30,
            "October" : 31,
            "November" : 30,
            "December" : 31,
        }
        if year>0:
            self.year=year
        else:
            self.year=2024
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            self.dates["February"]=29
        if 1<=month<=12:
            self.month=month
        else:
            self.month=1
        if 0<=day<= (list(self.dates.values())[self.month-1]):
            self.day=day
        else:
            self.day=1
            
        self.value = 365.2425 * self.year + 30.437 * self.month + day #To compare with other Dates. 
        # "Value" shows how many days AC is appr. equal to this date
        
    def __str__(self):
        return(f"{self.day} of {list(self.dates.keys())[self.month-1]} {self.year}")
    def next(self):
        if self.day+1<= (list(self.dates.values())[self.month-1]):
            return Date(self.day+1, self.month, self.year)
        if self.month+1<=12:
            return Date(1, self.month+1, self.year)
        return Date(1, 1, self.year+1)
    
# print (Date(20, 4).value > Date(19,4).value)
def next_date(d1, d2):
    if not (isinstance(d1, Date) and isinstance(d2, Date)):
        raise TypeError("Given parameters is not Dates")
    if d1.value>d2.value:
        raise ValueError("Dates have wrong order")
    while d1.value<=d2.value:
        yield d1
        d1=d1.next()
        
for d in next_date(Date(29, 12), Date(3, 1, 2025)):
    print(d)