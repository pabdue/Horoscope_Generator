#Names: Pablo Duenas & Olive Riggs

class Zodiac:
    def __init__(self, month, date):
        self.month = month
        self.date = date

    #the checkBirthday method will return True or False if user's month and date entry are int
    def checkBirthday(self):
        # first we check if user's input is able to convert to int
        try:
            self.month = int(self.month)
            self.date = int(self.date)
        except ValueError:
            #if the user input isnt convertible to int then ValueError exception is caught and function returns false
            return False

        # the follow elif statements view if the date corresponding to the month matches the range of calendar dates
        # ex) july = 7 date = 1-31
        if self.month == 1:
            if self.date >= 1 and self.date <= 31:
                return True
            else:
                return False
        elif self.month == 2:
            if self.date >= 1 and self.date <= 29:
                return True
            else:
                return False
        elif self.month == 3:
            if self.date >= 1 and self.date <= 31:
                return True
            else:
                return False
        elif self.month == 4:
            if self.date >= 1 and self.date <= 30:
                return True
            else:
                return False
        elif self.month == 5:
            if self.date >= 1 and self.date <= 31:
                return True
            else:
                return False
        elif self.month == 6:
            if self.date >= 1 and self.date <= 30:
                return True
            else:
                return False
        elif self.month == 7:
            if self.date >= 1 and self.date <= 31:
                return True
            else:
                return False
        elif self.month == 8:
            if self.date >= 1 and self.date <= 31:
                return True
            else:
                return False
        elif self.month == 9:
            if self.date >= 1 and self.date <= 30:
                return True
            else:
                return False
        elif self.month == 10:
            if self.date >= 1 and self.date <= 31:
                return True
            else:
                return False
        elif self.month == 11:
            if self.date >= 1 and self.date <= 30:
                return True
            else:
                return False
        elif self.month == 12:
            if self.date >= 1 and self.date <= 31:
                return True
            else:
                return False
        #if month isnt in range of 1-12 then return false for invalid input
        else:
            return False


    # zodiacSign method will return a String of the zodiac name if month and day are within the range of the
    # appropriate range of sign
    def zodiacSign(self):
        if self.month == 1:
            if self.date <= 19:
                return 'Capricorn'
            else:
                return 'Aquarius'
        elif self. month == 2:
            if self.date <= 20:
                return 'Aquarius'
            else:
                return 'Pisces'
        elif self.month == 3:
            if self.date <= 20:
                return 'Pisces'
            else:
                return 'Aries'
        elif self.month == 4:
            if self.date <= 20:
                return 'Aries'
            else:
                return 'Taurus'
        elif self.month == 5:
            if self.date <= 20:
                return 'Taurus'
            else:
                return 'Gemini'
        elif self.month == 6:
            if self.date <= 20:
                return 'Gemini'
            else:
                return 'Cancer'
        elif self.month == 7:
            if self.date <= 22:
                return 'Cancer'
            else:
                return 'Leo'
        elif self.month == 8:
            if self.date <= 22:
                return 'Leo'
            else:
                return 'Virgo'
        elif self.month == 9:
            if self.date <= 22:
                return 'Virgo'
            else:
                return 'Libra'
        elif self.month == 10:
            if self.date <= 22:
                return 'Libra'
            else:
                return 'Scorpio'
        elif self.month == 11:
            if self.date <= 22:
                return 'Scorpio'
            else:
                return 'Sagittarius'
        elif self.month == 12:
            if self.date <= 21:
                return 'Sagittarius'
            else:
                return 'Capricorn'

