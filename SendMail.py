from BudgetFlight import BudgetFlight
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail():

    my_message = BudgetFlight('Anywhere', 0, 0)
    sender_email = "poetrybot02@gmail.com"
    sender_password = "cutjqfpoaphszbdz"
    #receiver_email = "michalskit42@interia.pl"
    receiver_email = "kate.michalska7@gmail.com"

    subject = "Tanie loty"
    body = str(my_message)
    message = MIMEMultipart()
    message["From"] = 'Travel Bot'
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    server.sendmail(sender_email, receiver_email, message.as_string())

    server.quit()