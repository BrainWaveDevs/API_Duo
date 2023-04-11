#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━


app = Flask(__name__)


#━━━━━━━━━❮Endpoints❯━━━━━━━━━
@app.route('/hello', methods=['GET'])
def HelloWorld():
    return 'Hello World'

@app.route('/', methods=['GET', 'POST'])
def home():
    pred = None
    if request.method == 'POST':
        TotalCharges = np.float(request.form.get('TotalCharges'))
        MonthlyCharges = np.float(request.form.get('MonthlyCharges'))
        tenure = np.float(request.form.get('tenure'))
    return render_template('index.html', pred=pred)
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

if __name__ == '__main__':
     app.run(debug=True)