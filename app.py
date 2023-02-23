from flask import Flask, render_template, request
import os
from modelling import make_models
from joblib import load
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
rf = load('rf.joblib')
gbr, gbr_sc = load('gbr.joblib')
nn, nn_sc = load('nn.joblib')
print(gbr, gbr_sc)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        form = request.form
        f1 = float(request.form.get('slider1'))
        f2 = float(request.form.get('slider2'))
        f3 = float(request.form.get('slider3'))
        f4 = float(request.form.get('slider4'))
        f5 = float(request.form.get('slider5'))
        f6 = float(request.form.get('slider6'))

        feature_values = np.array([f1,f2,f3,f4,f5,f6]).reshape(1,-1)

     

        preds = make_models.makePreds([rf, gbr, nn], feature_values, [None, gbr_sc, nn_sc])

        value1 = round(preds[0],2)
        value2 = round(preds[1],2)
        value3 = round(preds[2],2)

        label1 = "Random Forest Regressor"
        label2 = "Gradient Boost Regressor"
        label3 = "Neural Network"

        return render_template('index.html', preds=preds, value1=value1, value2=value2,value3=value3,label1=label1,label2=label2,label3=label3)

    return render_template('index.html', preds=None)

@app.route('/modelling')
def modelling():
    return render_template('quality_prediction.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

