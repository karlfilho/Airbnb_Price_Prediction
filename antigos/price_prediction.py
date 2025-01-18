import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Carregar o dataset
file_path = 'datasets/cleaned_final_dataset.csv'
data = pd.read_csv(file_path)

# Remover a coluna 'roomURL'
data = data.drop(columns=['roomURL'])

# Identificar colunas categóricas e numéricas
categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
numerical_cols = data.select_dtypes(exclude=['object']).columns.tolist()
numerical_cols.remove('roomPrice')  # Excluir a variável alvo da normalização

# Criar um transformador de colunas com normalização para colunas numéricas e one-hot encoding para colunas categóricas
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Aplicar transformações
X = data.drop(columns=['roomPrice'])
y = data['roomPrice']
X_preprocessed = preprocessor.fit_transform(X)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

# Inicializar e treinar o modelo Random Forest
rf = RandomForestRegressor(n_estimators=200, max_depth=None, min_samples_split=5, min_samples_leaf=1, random_state=42)
rf.fit(X_train, y_train)

# Salvar o modelo Random Forest e o pré-processador
joblib.dump(rf, 'random_forest_model.pkl')
joblib.dump(preprocessor, 'preprocessor.pkl')

# Salvar os nomes das colunas para uso posterior
joblib.dump(numerical_cols, 'numerical_cols.pkl')
joblib.dump(categorical_cols, 'categorical_cols.pkl')
