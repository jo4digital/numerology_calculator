from dictionaries import numerology

class NumerBrain:
    def __init__(self):
        self.numer_dict = numerology

    def complete_sum(self, date_string):
        while len(date_string) > 1:
            date_string = str(sum(int(x) for x in date_string))
        return int(date_string)

    def numer_calc(self, date, age, month):
        birthdate_sum = self.complete_sum(date)
        date_and_age = str(birthdate_sum + int(age))
        final = self.complete_sum(date_and_age)
        if int(month) >= 7:
            if final == 9:
                final = 1
            else:
                final += 1
        return final
