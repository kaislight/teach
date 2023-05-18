from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import pandas as pd
data_file = "static/data.xlsx"

def register(request):
    data = pd.read_excel(data_file ,sheet_name= 'login')
    print(data)
    if request.method == 'GET':
        k_list = list(request.GET.keys())
        if (len(k_list) == 3):
            data[request.GET[k_list[0]]] = request.GET[k_list[1]]
            data.to_excel(data_file,sheet_name='login',index=False)
        if (len(k_list) == 1):
            data = data.drop(columns=[k_list[0]])
            print(data)
            data.to_excel(data_file,sheet_name='login',index=False)
    list_user = data.keys().tolist()
    dir_user = []
    for i in list_user:
        dir_user.append({'user': i ,'password': data[i][0]})
    return render(request, 'register/register.html', {'du': dir_user, 'user':request.session['user_id']})

def user_login(request):
    data = pd.read_excel(data_file ,sheet_name= 'login')
    list_user = data.keys().tolist()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username in list_user):
            print(data[username][0],password)
            if (str(data[username][0]) == str(password)):
                request.session['user_id'] = username
                return redirect('main')
            else:
                return render(request, 'register/login.html', {'error_message': '账号或密码错误'})
        else:
            return render(request, 'register/login.html', {'error_message': '账号或密码错误'})
    else:
        return render(request, 'register/login.html')

def user_logout(request):
    del request.session['user_id']
    return redirect('main')


def home(request):
    try:
        user = request.session['user_id']
    except:
        user = ""
    return render(request, 'home.html', {'user' : user})

def main(request):
    try:
        user = request.session['user_id']
    except:
        user = ""
    return render(request, 'main.html', {'user' : user})