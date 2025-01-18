import joblib
import pandas as pd
from sklearn.base import BaseEstimator

class PricePredictor:
    def __init__(self):
        self.model = None
        self.feature_names = None
    
    def load_model(self, model_path):
        self.model = joblib.load(model_path)
    
    def predict(self, features: dict) -> float:
        # Transformar input em formato adequado
        # Fazer predição
        # Retornar resultado
        pass 