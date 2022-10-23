from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Profile
import urllib.parse
import requests
import numpy as np
# from .apps import ohe, zip_code_keep, mlpc, sc
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


ohe = OneHotEncoder(sparse=False)
house_data = pd.read_csv('zipcodes.csv', low_memory=False)
house_data = house_data.astype({"address/zipcode": int})
zip_code_keep = house_data["address/zipcode"].unique()
zip_code = pd.DataFrame(ohe.fit_transform(
    house_data[['address/zipcode']])).astype('int32')
house_data = house_data.drop(columns=['address/zipcode'])
zip_code.reset_index(drop=True, inplace=True)
mlpc = pickle.load(open('./model2.sav', 'rb'))
sc = pickle.load(open('./scaler2.pkl', 'rb'))


def index(request):
    return render(request, 'homepage_3.html')


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                print("YES")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                print("NO")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id)
                new_profile.save()
                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect('dashboard')
                return redirect('signup')

        else:
            messages.info(request, 'Password Not Matching')
            print("NOT SURE")
            return redirect('signup')

    return render(request, "signin.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


prices = []


@login_required(login_url='signin')
def getlatlong(request):
    if request.method == 'POST':
        address = request.POST['address']

        """url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + \
            urllib.parse.quote(address) + \
            "&key=AIzaSyAURsn769ASDt8e5KxOKES3O4-AmztTjsI"
        response = requests.get(url).json()
        print(response['results'][0]['geometry']['location']['lat'])
        print(response['results'][0]['geometry']['location']['lng'])"""

        url = "https://zillow56.p.rapidapi.com/search"

        querystring = {"location": address}

        headers = {
            "X-RapidAPI-Key": "aadced3125msh3495c7ad216c030p14a0f3jsne47c45bc1a0f",
            "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring).json()
        if response.get('error'):
            print('bruh')
            messages.info(request, 'Location Not Found. Please re-enter')
            return redirect('index')

        try:
            school_rating = int(response['schools'][-1]['rating'])
            num_bedrooms = int(response['bedrooms'])
            num_bathrooms = int(response['bathrooms'])
            yearBuilt = int(response['yearBuilt'])
            zipcode = int(response['address']['zipcode'])
            livingArea = int(response['livingArea'])
            price = int(response['price'])
            rentZestimate = int(response['rentZestimate'])

            if zipcode not in zip_code_keep:
                print('exit')
                messages.info(request, 'Location Unavailable. Please re-enter')
                return redirect('index')

            l = [num_bathrooms, num_bedrooms,
                 livingArea, school_rating, yearBuilt]
            zip_trans = ohe.transform([[zipcode]])
            l = np.array(l).reshape(1, -1)
            l = np.concatenate((l, zip_trans), axis=1)
            x = sc.transform(l)
            y_pred = mlpc.predict(x)
            inflation = 1.1
            print(y_pred*inflation)

            # GRM - Gross Rent Multiplier
            grm = price/(rentZestimate * 12)

            # OPR - One Percent Rule
            opr = rentZestimate/price

            # Cap Rate
            capRate = ((rentZestimate*12) - (200))/(price)

            # NIAF - Net Income After Financing
            niaf = (rentZestimate*12) - (200)

            # COCR - Cash on Cash Return
            cocr = niaf/(.2*price)

            # temp = price history array

            priceHistory = response['priceHistory']
            temp = []
            for i in priceHistory:
                temp.append(i['price'])
            temp = [price] + temp
            temp.reverse()
            print(temp)
            prices = temp
            volatility = np.std(temp)
            print(volatility)
        except:
            messages.info(request, 'Data Unavailable. Please re-enter')

            return redirect('index')

    return render(request, 'dashboard.html', {'grm': grm, 'opr': opr, 'capRate': capRate, 'niaf': niaf, 'cocr': cocr, 'prices': temp, 'name': request.user.username})


@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.username})
