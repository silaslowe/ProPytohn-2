class Bill:
    """
    Object that contains data about bill such as amount or period of bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains data about flatmate
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight, 2)