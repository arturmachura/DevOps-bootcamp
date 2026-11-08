import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

try:
    response = requests.get('https://www.example.com')
    if response.status.code == 200:
        print('Website is up and running!')
    else:
    print('Application Down! Status code:', response.status_code)
    # send email to me
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.eghlo()
        smtp.login('EMAIL_ADDRESS', "EMAIL_PASSWORD")
        msg = "Subject: SITE DOWN! \n Fix the issue!"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

except Exception as ex:
     print(f'Connection error happened: {ex}')