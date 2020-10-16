
class year:

    def __init__(self, years):
        self.years = years

    def is_leap_year (self, years) :

        if years % 4 ==0 and years %400 == 0 :
            return "True"
        elif years % 100 != 0 :
            return "false"
        return "True"

