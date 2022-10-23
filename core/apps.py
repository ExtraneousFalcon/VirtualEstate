from django.apps import AppConfig
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import confusion_matrix, classification_report, r2_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
import pickle
import numpy as np

ohe = None
zip_code_keep = None
mlpc = None
sc = None


class CoreConfig(AppConfig):
    name = 'core'
    print("Hi")
    # ohe = OneHotEncoder(sparse=False)
    # house_data = pd.read_csv('HackGT2/HackGT/newyork_housing.csv', usecols=[
    #     'address/zipcode', 'bathrooms', 'bedrooms', 'livingArea', 'price', 'schools/0/rating', 'yearBuilt'], low_memory=False).dropna()
    # house_data = house_data.astype({"address/zipcode": int})
    # zip_code_keep = house_data["address/zipcode"].unique()
    # zip_code = pd.DataFrame(ohe.fit_transform(
    #     house_data[['address/zipcode']])).astype('int32')
    # house_data = house_data.drop(columns=['address/zipcode'])
    # zip_code.reset_index(drop=True, inplace=True)
    # mlpc = pickle.load(open('HackGT2/HackGT/model2.sav', 'rb'))
    # sc = pickle.load(open('HackGT2/HackGT/scaler2.pkl', 'rb'))
    print("initialized")
