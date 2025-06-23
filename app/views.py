# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):

    images = services.getAllImages()
    favourite_list = services.getAllFavorites(request)

    return render(request, 'home.html', {
        'images': images,
        'favourite_list': favourite_list
    })

# Función para el alta de usuarios. Crea un objeto User con los datos del formulario y envía un correo con las credenciales de acceso (usuario y contraseña).
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=username,
                password=password,
                email=email,
            )

            subject = 'Registro - Proyecto IP Pokedex'
            message = f'''
                Hola {firstname} {lastname},

                Gracias por registrarte en nuestra página.

                Credenciales de acceso:

                Usuario: {username}
                Contraseña: {password}

                Saludos!
                '''

            recipient = email
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Usuario registrado con éxito!')
            return redirect('register')
        else:
            if form.errors.get('username'):
                for e in form.errors['username']:
                    messages.error(request, e)
    return render(request, 'registration/register.html', {'form': form})

# función utilizada en el buscador.
def search(request):
    name = request.POST.get('query', '')

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name.strip() != ''):
        images = services.filterByCharacter(name)
        favourite_list = services.filterFavoritesByCharacter(request, name)

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# función utilizada para filtrar por el tipo del Pokemon
def filter_by_type(request):
    type = request.POST.get('type', '')

    if type != '':
        images = services.filterByType(type) # debe traer un listado filtrado de imágenes, segun si es o contiene ese tipo.
        favourite_list = services.filterFavoritesByType(request, type)

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = services.getAllFavorites(request)
    return render(request, 'favourites.html', {
        'favourite_list': favourite_list
    })

@login_required
def saveFavourite(request):
    if request.method == 'POST':
        services.saveFavourite(request)
    return redirect('home')

@login_required
def deleteFavourite(request):
    if request.method == 'POST':
        services.deleteFavourite(request)
    return redirect('favoritos')