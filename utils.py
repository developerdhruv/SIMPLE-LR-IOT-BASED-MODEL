import joblib
import numpy as np

def preprocess(CropDays, SoilMoisture, temperature, Humidity):
    
    CropDays = float(CropDays)
    SoilMoisture = float(SoilMoisture)
    temperature = float(temperature)
    Humidity = float(Humidity)
    
    
        
    test_data = np.array([[CropDays, SoilMoisture, temperature, Humidity]])
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)
    
    
    
    return prediction
    