from django.conf.urls import url, include
from . import views


urlpatterns = [

	url(r'^$', views.HomePage, name='HomePage'),
    url(r'^register/', views.RegisterPage, name='RegisterPage'),
    url(r'^getregister/', views.GetRegisterPage, name='getRegister'),

]
