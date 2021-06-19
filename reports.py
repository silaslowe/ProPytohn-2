import os.path
import webbrowser

from fpdf import FPDF


class PdfReport:
    """Creates PDF with info about how much each flatmate pays"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_paid = str(flatmate1.pays(bill, flatmate2))
        flatmate2_paid = str(flatmate2.pays(bill, flatmate1))

        pdf = FPDF(orientation='P', unit="pt", format="A4")
        pdf.add_page()
        pdf.image("files/house.png", w=30, h=30)
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

        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))
