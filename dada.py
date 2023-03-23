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

url = "file:///C:/Users/pytho/Documents/GitHub/API_Duo/templates/index.html"
response = requests.get(url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    html = response.text

    dfs = pd.read_html(html)
    df = dfs[0]

    df.to_excel("dados.xlsx", index=False)