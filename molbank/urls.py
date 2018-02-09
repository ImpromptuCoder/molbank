from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('molbank/<int:mol_id>/', views.detail),
    # path('molbank/',include('molbank.urls')),
    path('search',views.search_mol,name='search_mol'),
    path('index',views.index,name='index'),
    path('contact',views.contact, name='contact'),
    path('add_mols',views.add_mols, name='add_mols'),
    path('add',views.add, name='add'),
    path('login',views.loginHTML, name='login'),
]
