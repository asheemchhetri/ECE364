class TimeSpan:
    def __init__(self,weeks,days,hours):
        if type(weeks) is not int or type(days) is not int or type(hours) is not int:
            raise TypeError
        if weeks <0 or days <0 or hours<0:
            raise ValueError
        while hours >=24:
            days+=hours//24
            hours=hours%24
        while days >=7:
            weeks+=days//7
            days=days%7
        self.weeks=weeks
        self.days=days
        self.hours=hours

    def __str__(self):
        return str(format(self.weeks,'02d'))+"W "+str(self.days)+"D "+str(format(self.hours,'02d'))+"H"

    def getTotalHours(self):
        return self.weeks*(7*24)+self.days*24+self.hours

    def __add__(self, other):
        if type(other) is not TimeSpan or type(self) is not TimeSpan:
            raise TypeError
        return TimeSpan(self.weeks+other.weeks,self.days+other.days,self.hours+other.hours)

    def __mul__(self, other):


        if type(other) is int and type(self) is TimeSpan:
            if other <=0:
                raise ValueError
            else:

                return TimeSpan(self.weeks*other,self.days*other,self.hours*other)
        else:
            raise TypeError
    __rmul__=__mul__