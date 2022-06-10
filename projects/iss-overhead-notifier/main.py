import requests
import smtplib
import time
from datetime import datetime

LATITUDE = 18.4932340973463
LONGITUDE = -33.87678647548687
FROM_EMAIL = SENDER_EMAIL
PASSWORD = YOUR_PASSWORD
TO_EMAIL = RECEIVER_EMAIL


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"subject:Look up!\n\nThe ISS is above you in the sky!"
        )


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LATITUDE - 5 <= iss_latitude >= LATITUDE + 5 and LONGITUDE - 5 <= iss_longitude >= LONGITUDE + 5:
        return True


def is_night():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()
