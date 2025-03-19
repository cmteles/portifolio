from django.shortcuts import render, get_object_or_404, redirect
from . models import Course
from . models import About
from django.contrib import messages
from . forms import ContactForm


# Create your views here.

def home(request):
    courses = Course.objects.filter(situation=True).order_by('-id')
    return render(request, 'courses/home.html', {'courses': courses})

def course(request, slug):
    courses = Course.objects.filter(situation=True).order_by('-id')[:3]
    course = get_object_or_404(Course, slug=slug) 
    return render(request, 'courses/course.html', {'course': course,'courses': courses})

def about(request):
    abouts = About.objects.filter(situation=True).order_by('id')
    return render(request, 'courses/about.html', {'abouts': abouts})

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem Enviada!")
            return redirect('contact')
        else:
            messages.error(request, "Erro ao enviar!")

    else:
        form = ContactForm()    
    return render(request, 'courses/contact.html', {'form': form})
