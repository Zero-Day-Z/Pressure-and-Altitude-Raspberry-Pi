from Adafruit_BMP085 import BMP085
import smtplib

#Initialize Email
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = #email
GMAIL_PASSWORD = #password

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

# Initialise the BMP085 and use STANDARD mode (default value)
bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)
 
# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode
 
temp = bmp.readTemperature()
 
# Read the current barometric pressure level
pressure = bmp.readPressure()
 
# To calculate altitude based on an estimated mean sea level pressure
# (1013.25 hPa) call the function as follows, but this won't be very accurate
altitude = bmp.readAltitude()
 
# To specify a more accurate altitude, enter the correct mean sea level
# pressure level.  For example, if the current pressure level is 1023.50 hPa
# enter 102350 since we include two decimal places in the integer value
#current mean sea level according to google: 1013.25 hPa

altitude = bmp.readAltitude(101325)
pressure = (pressure / 100) 

print "Pressure:    %.2f hPa" % (pressure / 100.0)
print "Altitude:    %.2f" % altitude

sender = Emailer()
sendTo = #recipient email
emailSubject = "IOT Research: BMP180"
emailContent = "This is the Pi in the lab.\n Pressure and Altitude measurements below:\n Pressure: " +str(pressure) +"\nAltitude: "+str(altitude)
sender.sendmail(sendTo, emailSubject, emailContent)
