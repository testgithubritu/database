from django.contrib import admin

# Register your models here.
from . models import my_table

admin.site.register(my_table)