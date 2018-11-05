from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def contacto(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                #asunto, cuerpo, email de origen,email de destino, responder a
                "LIA Agrolaboratorio: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["jmavaldes@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #Todo ha ido bien
                return redirect(reverse('contacto')+'?ok')
            except:
                #Algo no ha salido bien, redireccionamos a FAIL
                return redirect(reverse('contacto')+'?fail')
                

    return render(request, 'core/contacto.html', {'form':contact_form})