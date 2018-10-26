from django.contrib import admin
from .models import Register
admin.autodiscover()

admin.site.register(Register)
# Register your models here.
