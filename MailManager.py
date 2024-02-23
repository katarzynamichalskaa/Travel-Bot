import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate
from FindFlights import FindFlights

class MailManager():

    def __init__(self, sender, sender_password, receiver):
        self.sender_email = sender
        self.sender_password = sender_password
        self.receiver_email = receiver

    def get_flights_info(self):

        params = {
            'srcAirport': 'Poznan[POZ]',
            'adults': 4,
            'depdate': '12.8.2024',
            'arrdate': '30.9.2024',
            'maxDaysStay': 10,
            'currency': 'PLN'
        }

        flights = FindFlights()
        flights.generate_url({**flights.default_params, **params})
        return flights.find_()

    def create_message(self):
        flights_info = self.get_flights_info()

        table = tabulate(flights_info, headers=["Price & Length of Stay", "Departure", "Arrival", "Link"], tablefmt="psql")

        return f"Hello!\n\nHere are some cheap flights for you:\n\n{table}"

    def send(self):
        subject = "Cheap flights"
        message_body = self.create_message()

        message = MIMEMultipart()

        message["From"] = 'Travel Bot'
        message["To"] = self.receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(message_body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            server.quit()