class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year
        self.yeardays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if self.isLeapYear():
            self.yeardays[2] = 29

    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s = "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s

    def __eq__(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if (self.year == d2.year) and (self.month == d2.month) and (self.day == d2.day):
            return True
        else:
            return False

    def __lt__(self, d2):
        """
        :param d2: another Date object
        :return: Returns True iff self is before d2
        """
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                elif self.day == d2.day:
                    return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, d2):
        """
        :return: Returns True iff d1 is after d2
        """
        if (self.year == d2.year) and (self.month == d2.month) and (self.day == d2.day):
            return False
        else:
            return not(self.isBefore(d2))

    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise.
        """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def tomorrow(self):
        """
        :return: Incriments the date by 1 day
        """
        self.day += 1
        if self.day > self.yeardays[self.month]:
            self.day = 1
            self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
            if self.isLeapYear():
                self.yeardays[2] = 29
            else:
                self.yeardays[2] = 28

    def yesterday(self):
        """
        :return: Incriments the day back 1
        """
        self.day -= 1
        if self.day == 0:
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.year -= 1
            self.day = self.yeardays[self.month]
            if self.isLeapYear():
                self.yeardays[2] = 29
            else:
                self.yeardays[2] = 28

    def addNDays(self, N):
        """
        :param N: Number of days to add
        :return: Adds N days to the date and prints the dates along the way
        """
        print self
        for i in range(1, N + 1):
            self.tomorrow()
            print self

    def subNDays(self, N):
        """
        :param N: Number of days
        :return: Subtracts N days, printing along the way
        """
        print self
        for i in range(1, N + 1):
            self.yesterday()
            print self

    def isBefore(self, d2):
        """
        :param d2: another Date object
        :return: Returns True iff self is before d2
        """
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                elif self.day == d2.day:
                    return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def isAfter(self, d2):
        """
        :return: Returns True iff d1 is after d2
        """
        if (self.year == d2.year) and (self.month == d2.month) and (self.day == d2.day):
            return False
        else:
            return not(self.isBefore(d2))

    def diff(self, d2):
        """
        :return: returns the difference between two dates in days
        """
        positive = (self > d2)
        day1 = Date(self.month, self.day, self.year)
        day2 = Date(d2.month, d2.day, d2.year)
        difference = 0
        if day1 == day2:
            return 0
        else:
            if positive == True:
                while day1 > day2:
                    difference += 1
                    day2.tomorrow()
                return difference
            else:
                while day1 < day2:
                    difference += 1
                    day1.tomorrow()
                return difference * -1

    def dow(self):
        """
        :return: returns the day of the week
        """
        comparitor = Date(3, 9, 2016)
        daydiff = self.diff(comparitor)
        dowdiff = daydiff%7
        newdow = (dowdiff + 2)%7
        return self.weekdays[newdow]

    def dow2(self, refDate):
        if refDate.dow() == "Wednesday":
            comparitor = refDate
            daydiff = self.diff(comparitor)
            dowdiff = daydiff%7
            newdow = (dowdiff + 2)%7
            return self.weekdays[newdow]
        else:
            return False

"""
date = Date(2, 28, 2016)
date2 = Date(12, 31, 2016)
date3 = Date(11, 30, 2016)
date4 = Date(1, 1, 0001)
date5 = Date(3, 10, 2016)
date6 = Date(3, 10, 2015)
date.tomorrow()
date2.tomorrow()
date3.tomorrow()
date.yesterday()
date2.yesterday()
date3.yesterday()
date4.addNDays(2)
date4.subNDays(2)
print date
print date2
print date3
print date.isBefore(date2)
print date.isAfter(date2)
print date2.isBefore(date2)
print date2.isAfter(date)
print date.isBefore(date2)
print date2.isAfter(date)
print date2.diff(date)
print date.diff(date2)
print date5.dow()
print date6.dow()
"""

def nycounter():
    """Looking ahead to 100 years of New Year's celebrations"""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # live for another 100 years
    for year in range(2014, 2115):
        d = Date(1, 1, year)   # get ny
        # print 'Current date is', d
        s = d.dow()        # get day of week
        dowd[s] += 1       # count it

    print 'totals are', dowd

def bdcounter():
    """Looking ahead to 100 years of Birthday celebrations"""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # live for another 100 years
    for year in range(2014, 2115):
        d = Date(4, 7, year)   # get ny
        # print 'Current date is', d
        s = d.dow()        # get day of week
        dowd[s] += 1       # count it

    print 'totals are', dowd

def badluck13():
    """Looking ahead to 100 years of New Year's celebrations"""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0
    reference = Date(8,13,2014)

    # live for another 100 years
    for year in range(2014, 2415):
        for month in range(1, 13):
            d = Date(month, 13, year)   # get ny
            print 'Current date is', d
            s = d.dow2(reference)        # get day of week
            if s == "Wednesday":
                reference = d
            dowd[s] += 1       # count it

    print 'totals are', dowd

# nycounter()
# bdcounter()
badluck13()
