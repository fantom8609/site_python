from django import forms
from .models import *

class SubscriberForm(forms.ModelForm): # ДЕЛАЕМ ФОРМУ НА ОСНОВЕ МОДЕЛИ
    class Meta:
        model = Subscribers
        exclude = [""]