from django.urls import path
from . import views

urlpatterns=[
  path('',views.Table_show)

]