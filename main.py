from flat import Bill, Flatmate
from reports import PdfReport

a = float(input("Hey, enter bill amount: "))

period_span = input("Enter the period for bill: ")

user_1_name = input("Say flatmate 1's name: ")
user_1_days_in_house = float(input("Say flatmate 1's days in house: "))

user_2_name = input("Say flatmate 2's name: ")
user_2_days_in_house = float(input("Say flatmate 2's days in house: "))

the_bill = Bill(a, period_span)
john = Flatmate(user_1_name, user_1_days_in_house)
marry = Flatmate(user_2_name, user_2_days_in_house)

# print(john.pays(the_bill, marry))
# print(marry.pays(the_bill, john))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
