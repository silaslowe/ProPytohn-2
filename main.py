import os.path
import webbrowser

from fpdf import FPDF


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


class PdfReport:
    """Creates PDF with info about how much each flatmate pays"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_paid = str(flatmate1.pays(bill, flatmate2))
        flatmate2_paid = str(flatmate2.pays(bill, flatmate1))

        pdf = FPDF(orientation='P', unit="pt", format="A4")
        pdf.add_page()
        pdf.image("house.png", w=30, h=30)
        # Set title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family="Times", size=10)
        # Insert first flatmate
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=f"${flatmate1_paid}", border=0, ln=1)

        # Insert second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=f"${flatmate2_paid}", border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open('file://'+os.path.realpath(self.filename))


the_bill = Bill(120, "April 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.pays(the_bill, marry))
print(marry.pays(the_bill, john))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
