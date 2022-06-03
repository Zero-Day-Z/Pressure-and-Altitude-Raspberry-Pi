import Adafruit_BMP.BMP085 as BMP085
import smtplib
import time

#sensor
sensor = BMP085.BMP085()
#Initialize Email
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = #Enter login email here
GMAIL_PASSWORD =  #Enter password to email here

class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
            "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
while True:
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()
    pressure = round(pressure, 2)
    altitude = round(altitude, 2)
    print(pressure,"Pa")
    print(altitude, "m")

    sender = Emailer()
    sendTo = #Enter recipient email here
    emailSubject = "IOT Research: BMP180"
    emailContent = "This is the Pi in the lab.\n Pressure and Altitude measurements below:\n Pressure: " +str(pressure) +"\nAltitude: "+str(altitude)
    sender.sendmail(sendTo, emailSubject, emailContent)
    time.sleep(2)

