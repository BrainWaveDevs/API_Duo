#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import unicodedata
import time
import pandas as pd
import requests
from flask import Flask, jsonify, request, render_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from mimetypes import add_type
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#━━━━━━━━❮envio do Email❯━━━━━━━━━
def enviar_email():
    time.sleep(1)
    body = f"""
    Teste de cria
    """

    sender = 'settlinksp@gmail.com'
    password = 'jmolibocyyhmgqxv'
    receiver = 'brainwavedev.ai@gmail.com'


    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'teste de api tchelogx'

    message.attach(MIMEText(body, 'plain'))

    pdfname = f'Secure_{relt}.pdf'


    binary_pdf = open(pdfname, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())

    encoders.encode_base64(payload)

    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)

    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls()

    session.login(sender, password)

    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('200')
    time.sleep(1)
#━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━