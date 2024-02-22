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
        flights = FindFlights("https://www.azair.eu/azfin.php?searchtype=nonflexi&tp=0&isOneway=return&srcAirport=Poznan+%5BPOZ%5D&srcFreeAirport=&srcTypedText=pozn&srcFreeTypedText=&srcMC=&dstAirport=Anywhere+%5BXXX%5D&anywhere=true&dstTypedText=any&dstFreeTypedText=&dstMC=&depmonth=202408&depdate=2024-08-11&aid=0&arrmonth=202408&arrdate=2024-08-25&plus5=true&minDaysStay=2&maxDaysStay=8&dep0=true&dep1=true&dep2=true&dep3=true&dep4=true&dep5=true&dep6=true&arr0=true&arr1=true&arr2=true&arr3=true&arr4=true&arr5=true&arr6=true&samedep=true&samearr=true&minHourStay=0%3A45&maxHourStay=16%3A30&minHourOutbound=0%3A00&maxHourOutbound=24%3A00&minHourInbound=0%3A00&maxHourInbound=24%3A00&autoprice=true&adults=4&children=0&infants=0&maxChng=1&currency=PLN&lang=en&indexSubmit=Search")
        return flights.find_()

    def create_message(self):
        flights_info = self.get_flights_info()

        table = tabulate(flights_info, headers=["Price & Length of Stay", "Departure", "Arrival", "Link"], tablefmt="psql")

        return f"Hello!\n\nHere are some cheap flights for you:\n\n{table}"

    def send(self):
        subject = "Tanie loty"
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