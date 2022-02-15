from fpdf import FPDF
import webbrowser
import os
from filestack import Client


class PdfReport:

    # create a pdf file that contains data about the flatmates such as 
    # their names, their due amounts and the period of the bill

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill,flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill,flatmate1),2))


        

        pdf = FPDF(orientation = 'P', unit = 'pt', format = 'A4')
        pdf.add_page()

        # add icon
        pdf.image('files/house.png', w=30, h=30)

        # insert title
        pdf.set_font(family='Times', size=24, style='I')

        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1 )
        # pdf.output('bill.pdf')

        # Insert  name and due amount of the first flatmate
        
        pdf.set_font(family='Times', size=12)

        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0, ln=1)




        #change directory to files, generate and open the pdf
        os.chdir('files')           #taki pdf files m save ho



        pdf.output(self.filename)
        webbrowser.open(self.filename)        #ye line automatically pdf khol deti h hamare liye
                                              #hume webbrowser import karna padega




#upload files to the cloud

class FileSharer:
    def __init__(self, filepath, api_key='AM3AZFE9tQ9aA1itWNbuVz'):   #copy from filestack.com
        self.filepath = filepath
        self.api_key = api_key


    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url