from django.shortcuts import render, redirect
from .models import About, Contact
from .forms import ContactForm
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    about_list = About.objects.all()
    return render(request, 'main/about.html', context={
        'about_list':about_list
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('message')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', context={'form':form})


def message(request):
    return render(request, 'main/message.html')