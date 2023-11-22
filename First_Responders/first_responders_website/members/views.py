from django.shortcuts import render
from django.http import HttpResponse
from .models import Members

def members(request):
    users = Members.objects.all()
    return render(request, "base.html",{"members": users})