# from datetime import time
import time

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
# from . migrate import *
import pandas as pd
import requests
from .models import Customer

# Create your views here.
a=''
def home(request):
    return render(request,'index.html')
def upload_file(request):
    global a
    file = request.FILES['filefield']
    print(file)
    df = pd.read_excel(file, engine='openpyxl')
    a = df
    return render(request,'dropdown.html',{'allcolumns':list(df.columns)})

def select(request):
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
    company = request.POST['select']
    first_name = request.POST['select1']
    last_name = request.POST['select2']
    phone = request.POST['select3']
    email = request.POST['select4']
    notes = request.POST['select5']
    address1 = request.POST['select6']
    address2= request.POST['select7']
    address_type= request.POST['select8']
    address_city= request.POST['select9']
    address_company= request.POST['select10']
    country_code= request.POST['select11']
    address_fname= request.POST['select12']
    address_lname= request.POST['select13']
    address_phone= request.POST['select14']
    postal_code= request.POST['select15']
    state_or_province= request.POST['select16']
    for index,row in a.iterrows():
        payload =[{
                "company": row[company],
                "first_name": row[first_name],
                "last_name": row[last_name],
                "phone": str(row[phone]),
                "email": row[email],
                "notes": row[notes],
                "addresses":[
                    {
                        # "address_type": row[address_type],

                        "address_fname": row[address_fname],
                        "address_lname": row[address_lname],
                        "address_company": row[address_company],
                        "address_phone": str(row[address_phone]),
                        "address_city": row[address_city],
                        "country_code": row[country_code],
                        "address1": row[address1],
                        # "address2": row[address2],

                        "postal_code": row[postal_code],
                        "state_or_province": row[state_or_province]
                    }
            ]
        }]
        print(payload)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
    return home(request)