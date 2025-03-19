from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import About
from .models import ContactMessage

# Register your models here.
from .models import Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'original_price', 'discounted_price')
    name = 'courses'
    verbose_name = 'cursos'

    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    name = 'about'
    verbose_name = 'sobre'

    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }

@admin.register(ContactMessage)
class ContactMessageeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    name = 'contact_message'
    verbose_name = 'mensagem de contato'