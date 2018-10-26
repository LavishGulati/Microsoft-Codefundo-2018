from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import Register, Request
from .forms import RegisterForm, RequestForm
import requests


def HomePage(request):
	return render(request,'forms/homepage.html')

def ContributePage(request):
	return render(request,'forms/toContri.html')

def ContactPage(request):
	return render(request,'forms/contactInfo.html')

def GetRegisterPage(request):
	all_registers = Register.objects.all()
	context={'all_registers' : all_registers,}
	return render(request,'forms/getReg.html',context)

def GetRequestPage(request):
	all_requests = request.objects.all()
	context={'all_requests' : all_requests,}
	return render(request,'forms/getReq.html',context)

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

def RequestPage(request):
	if request.method == "POST":
		form = RequestForm(request.POST)
		if form.is_valid():
			obj = Request()
			obj.name = form.cleaned_data['name']
			obj.contact = form.cleaned_data['contact']
			obj.location = form.cleaned_data['location']
			obj.assistance = form.cleaned_data['assistance']
			obj.special = form.cleaned_data['special']
			obj.housing = form.cleaned_data['housing']
			obj.priority = form.cleaned_data['priority']
			obj.save()
			return HttpResponseRedirect('/')

	else:
		form = RequestForm()

	return render(request,"forms/reqForHelp.html", {'form' : form})


	


	