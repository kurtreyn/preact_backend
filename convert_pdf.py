from fpdf import FPDF
import os
from config.definitions import ROOT_DIR
import datetime
import phonenumbers as pn
from create_email import create_email


cw = 40
# standard cell height
ch = 8
# full width of page
cfw = 200

# standard padding cell width
cpw = 30
# standard padding cell height
cph = 8


the_content = {
	"form_id": "123456789",
	"date": "2023-01-04",
	"name": "Kurt",
	"email": "kurt@reynaissance.com",
}


class PDF(FPDF):
	def header(self):
		# Font
		self.set_font('arial', "B", 14)
		# Padding
		self.cell(20)
		# Title
		self.multi_cell(180, 10, "A note of gratitude for trying out @KurtReyn's Preact & Python/Flask Demo", border=False, align="C")
		# Line Break
		self.ln(12)

	def footer(self):
		self.set_y(-15)
		self.set_font('arial', "B", 10)
		self.cell(0, 10, f"page {self.page_no()}/{{nb}}", align='C')


def create_pdf(content):
	# ---------- DOCUMENT PAGE SETUP
	pdf = PDF("P", "mm", "Letter")
	pdf.alias_nb_pages()
	pdf.set_margins(left=10, top=5, right=10)
	pdf.set_auto_page_break(auto=True, margin=15)
	pdf.add_page()

	form_id = content["form_id"]
	date = content["date"]
	name = content["name"]
	email = content["email"]
	message = content["message"]

	print(f"content: {content}")

	# ---------- SECTION TITLE
	pdf.set_font("arial", "B", 12, )
	pdf.cell(40, 10, f"Thank you for visiting, {name}", ln=True)

	# ---------- CUSTOMER INFORMATION SECTION
	pdf.set_font("arial", "B", 11, )
	pdf.cell(40, 8, "Date:")
	pdf.set_font("arial", "", 11, )
	pdf.cell(40, 8, date, ln=True)

	pdf.set_font("arial", "B", 11, )
	pdf.cell(40, 8, "Name:")
	pdf.set_font("arial", "", 11, )
	pdf.cell(40, 8, name, ln=True)

	pdf.set_font("arial", "B", 11, )
	pdf.cell(40, 8, "Email:")
	pdf.set_font("arial", "", 11, )
	pdf.cell(40, 8, email, ln=True)

	pdf.set_font("arial", "B", 11, )
	pdf.cell(40, 8, "Your message:")
	pdf.set_font("arial", "", 11, )
	pdf.cell(100, 16, message, ln=True)

	pdf.ln(4)

	# ---------- SAVE PDF

	directory = f"{ROOT_DIR}/sent-pdf"
	file = f"{form_id}.pdf"
	file_path = os.path.join(directory, file)
	app_file = pdf.output(file_path)
	return app_file

# create_pdf(the_content)


