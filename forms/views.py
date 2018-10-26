from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import Register
from .forms import RegisterForm
import requests



def HomePage(request):
	return render(request,'forms/homepage.html')

def GetRegisterPage(request):
	all_registers = Register.objects.all()
	context={'all_registers' : all_registers,}
	return render(request,'forms/getReg.html',context)

def RegisterPage(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			obj = Register()
			obj.name = form.cleaned_data['name']
			obj.contact = form.cleaned_data['contact']
			obj.message = form.cleaned_data['message']
			obj.location = form.cleaned_data['location']
			obj.profession = form.cleaned_data['profession']
			obj.save()
			return HttpResponseRedirect('/')

	else:
		form = RegisterForm()


	return render(request,"forms/regAsVol.html", {'form' : form})
