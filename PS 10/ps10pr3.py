#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# A class to represent calendar dates
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
        """
    
    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes
            in every Date object (month, day, and year)
            """
    # add the necessary assignment statements below
        self.m = 0
        self.d = 0
        self.y = 0
        self.month = init_month
        self.day = init_day
        self.year = init_year
    
    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).
            
            ** Note that this _can_ be called explicitly, but
            it more often is used implicitly via printing or evaluating.
            """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s
    
    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
            """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
            """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####

# 3.
    def advance_one(self):
        """ Changes the called object so that it represents one calendar day
            after the date that it originally represented.
            Nothing is returned.
            """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.d = 1
        self.day += self.d
        if self.day > days_in_month[self.month]:
            self.m = 1
            self.month += self.m
            self.day = 1
            if self.month == len(days_in_month):
                self.y = 1
                self.year += self.y
                self.month = 1

# 4.
    def advance_n(self, n):
        """ Changes the calling object so that it represents n calendar days
            it originally represented. Method will print all of the dates
            from the starting date to the finishing date, inclusive of both
            endpoints.
            """
        print(self)
        for a in range(n):
            self.advance_one()
            print(self)

# 5.
    def __eq__(self, other):
        """ Returns True if the called object (self) and the argument (other)
            represent the same calendar date (i.e., if the have the same values
            for their day, month, and year attributes). Otherwise, this method
            should return False.
            """
        if self.month == other.month and self.day == other.day and self.year == other.year:
            return True
        else:
            return False

# 6.
    def is_before(self, other):
        """ Returns True if the called object represents a calendar date that occurs
            before the calendar date that is represented by other.
            If self and other represent the same day, or if self occurs after other,
            the method should return False.
            """
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

# 7.
    def is_after(self, other):
        """ Returns True if the calling object represents a calendar date that occurs
            after the calendar date that is represented by other.
            If self and other represent the same day, or if self occurs before other,
            the method should return False.
            """
        if other.is_before(self) is True:
            return True
        else:
            return False

# 8.
    def days_between(self, other):
        """ Returns an integer that represents the number of days
            between self and other.
            """
        self_copy = self.copy()
        other_copy = other.copy()
        count = 0
        if self_copy.is_leap_year() == True or other_copy.is_leap_year() == True:
            if self_copy.is_before(other_copy) == True:
                count -= 1
            elif self_copy.is_after(other_copy) == True:
                count += 1
        while self_copy != other_copy:
            if self_copy.is_before(other_copy) == True:
                self_copy.advance_one()
                count -= 1
            elif self_copy.is_after(other_copy) == True:
                other_copy.advance_one()
                count += 1
        return count

# 9.
    def day_name(self):
        """ Returns a string that indicates the name of the day of the week
            of the Date object that calls it.
            """
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        known_date = Date(7, 22, 2019)
        n = self.days_between(known_date)
        remainder = n % 7
        if n == 0:
            return day_names[remainder]
        elif n < 0:
            if remainder <= 3:
                return day_names[0 - (7 - remainder)]
            else:
                return day_names[0 - remainder]
        elif n > 0:
            return day_names[remainder]
