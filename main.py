import smtplib
from email.message import EmailMessage

def sendMail(toaddr, subject, body):
	msg = EmailMessage()
	msg.set_content(body)

	msg['Subject'] = subject
	msg['From'] = FROM_ADDR
	msg['To'] = toaddr

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(FROM_ADDR, FROM_PASSWD)
	s.send_message(msg)
	s.quit()


inp = list(input("What to spam: "))

addr = input("Who to spam: ")

for x in range(0, len(inp)):
	sendMail(addr, inp[x], inp[x])
