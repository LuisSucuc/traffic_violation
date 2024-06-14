import requests
from django.shortcuts import render

host = 'http://localhost:8000'


def home_view(request):
    return render(request, 'home.html')


def view_infraction_records(request):
    infractions = []
    email = request.POST.get('email', '')

    if request.method == "POST" and email:
        response = requests.get(f'{host}/api/infractions/generar_informe/',
                                params={'email': email})
        if response.status_code == 200:
            infractions = response.json()

    return render(request, 'my_infractions.html', {'infractions': infractions, 'email': email})


def view_create_infraction(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    response = None
    error = False

    if request.method == "POST":
        if username and password:
            response = requests.post(f'{host}/api/token/',
                                     json={'username': username, 'password': password})
            if response.status_code != 200:
                error = True


    return render(request, 'create_infraction.html',
                  {'username': username, 'token': response.json() if response else response, 'error': error})
