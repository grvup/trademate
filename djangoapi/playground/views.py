# views.py

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse,HttpResponse
# from tensorflow.keras.layers import LSTM
from tensorflow.keras.initializers import glorot_uniform

from playground.models import User
from playground.serializers import UsersSerializer
from django.db import close_old_connections
import pandas as pd
import joblib
# import pickle
from tensorflow.keras.models import model_from_json
# from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Bidirectional, LSTM, Dense
# from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
# from custom_layers import CustomOrthogonal
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.callbacks import ModelCheckpoint
import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
import numpy as np


# Modelpath  = 'C:/Users/gaura/pr/seperate Files/A_model.keras'
Modelpath = 'C:/Users/gaura/OneDrive/Desktop/Pr/models/AKAM_stock_lstm_model.keras'


model = load_model(Modelpath)

@csrf_exempt
def register_user(request):
    if request.method=='GET':
        users = User.objects.all()
        user_seri = UsersSerializer(users,many=True)
        return JsonResponse(user_seri.data,safe=False)
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        print(user_data)
        email = user_data['email']
        password  =user_data['password']
        cnfpassword = user_data['confirmPassword']
        print(email)
        user_seri = UsersSerializer(data = user_data)
        if password == cnfpassword:
            if user_seri.is_valid():
                user_seri.save()
                return JsonResponse("Added Successfully",safe = False)
            return JsonResponse("Failed to add",safe=False)
        return JsonResponse("password not match",safe=False)


# def predict_stocks(request):
#     if request.method == 'POST':
#         file = request.FILES['file']


        



# Create your views here.
