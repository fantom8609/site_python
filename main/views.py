from django.shortcuts import render
from .forms import SubscriberForm
from django.shortcuts import render
# Create your views here.

def index(request):
    name = "Denis"
    form = SubscriberForm(request.POST or None)
    return render(request, "main/index.html", locals())
