import warnings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
warnings.simplefilter("ignore")


class SendPdf:
	def __init__(self, sender_email, receiver_email, receiver_bcc, sender_password, subject, body, file_name, address_of_file):
		self.sender_email = sender_email
		self.receiver_email = receiver_email
		self.receiver_bcc_email = receiver_bcc
		self.sender_password = sender_password
		self.subject = subject
		self.body = body
		self.file_name = file_name
		self.address_of_file = address_of_file

	def email_send(self):
		from_addr = self.sender_email
		to_addr = self.receiver_email
		to_bcc = self.receiver_bcc_email

		msg = MIMEMultipart()
		msg['From'] = from_addr
		msg['To'] = to_addr
		msg['Bcc'] = to_bcc
		msg['Subject'] = self.subject
		body = self.body
		msg.attach(MIMEText(body, 'plain'))

		filename = self.file_name
		attachment = open(f"{self.address_of_file}/{self.file_name}.pdf", "rb")

		payload = MIMEBase('application', _subtype='pdf')
		payload.set_payload(attachment.read())
		encoders.encode_base64(payload)
		payload.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		msg.attach(payload)

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(from_addr, self.sender_password)
		text = msg.as_string()
		server.send_message(msg, from_addr, to_addrs={to_addr, to_bcc})
		server.quit()


def create_email(file_name, file_path, sender, sender_email):
	password = "erpqdhqxaiqqldrs"
	from_addr = "kurttempemailaddress@gmail.com"
	to_addr = f"{sender_email}"
	to_bcc = f"{from_addr}"
	subject = f'New App from: {sender} '
	body =  "Thank you for visiting KurtReyn's Preact & Python/Flask Demo. A PDF was attached to this message"
	print(f"SENDING EMAIL TO: {to_addr}, BCC: ${to_bcc}")
	details = SendPdf(
		from_addr,
		to_addr,
		to_bcc,
		password,
		subject,
		body,
		file_name,
		file_path
	)
	details.email_send()
	return True