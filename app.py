from logging import debug
from flask import Flask, render_template, request
import utils
from flask import request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        CropDays = request.form.get('CropDays')
        SoilMoisture = request.form.get('SoilMoisture') 
        temperature = request.form.get('temperature')
        Humidity = request.form.get('Humidity')
        
    
    prediction = utils.preprocess(CropDays, SoilMoisture, temperature, Humidity)
    
    return render_template('prediction.html', prediction=prediction)    

if __name__ == "__main__":
    app.run(debug=True)
    