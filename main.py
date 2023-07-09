from SendMail import send_mail
import time
import schedule

schedule.every().sunday.at("11:40").do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(1)
