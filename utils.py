import joblib
import numpy as np

def preprocess(Open, High, Low, Volume, Adjclose):
    
    Open = float(Open)
    High = float(High)
    Low = float(Low)
    Volume = float(Volume)
    Adjclose = float(Adjclose)
    
        
    test_data = np.array([[Open, High, Low, Volume, Adjclose]])
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)
    
    
    
    return prediction
    