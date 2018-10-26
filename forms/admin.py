from django.contrib import admin
from .models import Register, Request
admin.autodiscover()

admin.site.register(Register)
admin.site.register(Request)
# Register your models here.
