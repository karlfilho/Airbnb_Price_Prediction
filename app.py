import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo e o pré-processador
model = joblib.load('random_forest_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Layout da página
st.title("Previsão de Preço para Acomodações")

# Criar campos de entrada para categorias específicas
room_type = st.selectbox('Tipo de Quarto', options=['Loft', 'Chalé', 'Quarto', 'Cabana', 'Contêiner', 'Microcasa', 'Casa', 'Apartamento', 'Pousada', 'Hotel', 'Condomínio', 'Suíte', 'Lugar', 'Trailer'], key='roomType')
quality_badge = st.selectbox('Qualidade', options=['superhost', 'preferido', 'no_class'], key='qualityBadge')
rating = st.number_input('Avaliação', min_value=0.0, max_value=5.0, value=4.5, step=0.01, key='rating')
count_reviews = st.number_input('Número de Avaliações', min_value=0, max_value=507, value=50, key='countReviews')

# Definir a lista de colunas de amenidades
amenities_columns = [
    'Air Conditioning', 'TV', 'Hair Dryer', 'Bathroom', 'Ethernet connection',
    'Kitchen', 'Elevator', 'Luggage Dropoff Allowed', 'Smoke Alarm', 'WiFi',
    'Parking', 'Pets Allowed', 'EV Charger', 'Bedroom', 'Fire pit',
    'Lit path to the guest entrance', 'Waterfront', 'Long term stays allowed',
    'Bathtub', 'Laundry room', 'Security Cameras', 'Baby bath', 'Pool',
    'Microwave', 'HDTV', 'View', 'Carbon Monoxide Alarm', 'Refrigerator',
    'Smoking allowed', 'Patio', 'High Chair', 'Sauna', 'Crib', 'Washer',
    'Accessible', 'Breakfast'
]

# Adicionar variáveis de amenidades
amenities = {col: st.checkbox(col) for col in amenities_columns}
is_new = st.radio('É novo?', ['Sim', 'Não'], index=0, key='isNew')

# Preparar dados para previsão
input_data = pd.DataFrame({
    'roomType': [room_type],
    'qualityBadge': [quality_badge],
    'rating': [rating],
    'countReviews': [count_reviews],
    **{col: [1 if amenities[col] else 0] for col in amenities_columns},
    'is_new': [1 if is_new == 'Sim' else 0]
})

# Converter dados categóricos e numéricos conforme necessário
input_preprocessed = preprocessor.transform(input_data)

# Botão para realizar a previsão
if st.button('Prever Preço'):
    prediction = model.predict(input_preprocessed)
    st.write(f"Preço estimado: R$ {prediction[0]:.2f}")