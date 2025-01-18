import tkinter as tk
from tkinter import ttk
import pandas as pd
from src.models.model import PricePredictor
from src.data.data_loader import DataProcessor

class AirbnbPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Preditor de Preços Airbnb - Campos do Jordão")
        self.model = PricePredictor()
        
        # Interface básica
        self.setup_ui()
    
    def setup_ui(self):
        # Criar campos de entrada para as features principais
        # Botão de predição
        # Área de resultado
        pass

    def predict(self):
        # Lógica de predição
        pass

def main():
    root = tk.Tk()
    app = AirbnbPredictorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 