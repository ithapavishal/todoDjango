from django.contrib import admin
from django.urls import path

from todoapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', home, name='home'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name = 'edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete-all/', delete, name='delete_all'),

    # path('delete-all/', delete_all, name='delete_all'),

]
