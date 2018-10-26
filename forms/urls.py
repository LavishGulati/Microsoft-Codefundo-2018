from django.conf.urls import url, include
from . import views


urlpatterns = [

	url(r'^$', views.HomePage, name='HomePage'),
    url(r'^register/', views.RegisterPage, name='RegisterPage'),
    url(r'^getregister/', views.GetRegisterPage, name='getRegister'),
    url(r'^contribute/', views.ContributePage, name='ContributePage'),
    url(r'^contact/', views.ContactPage, name='ContactPage'),
    url(r'^request/', views.RequestPage, name='RequestPage'),
    url(r'^getrequest/', views.GetRequestPage, name='getRequest'),

]
