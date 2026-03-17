import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    return pd.read_csv(file_path)

def split_data(data, test_size=0.2, random_state=42):
    X = data.drop('target', axis=1)
    y = data['target']
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def save_model(model, file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    with open(file_path, 'wb') as f:
        f.write(model.to_bytes())

def load_model(file_path):
    with open(file_path, 'rb') as f:
        return np.frombuffer(f.read(), dtype=np.float32).reshape(-1, 1)

def normalize_data(data):
    return (data - data.mean()) / data.std()