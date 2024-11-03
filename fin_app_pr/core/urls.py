"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
import catalog.views 



urlpatterns = [
    path('', catalog.views.main, name='main'),
    path('categories', catalog.views.categories, name='categories'),
    path('budgets', catalog.views.budgets, name='budgets'),
    path('products/', catalog.views.products_view, name='products'),
    path('lunches', catalog.views.lunches_view, name='lunches'),
    path('cloth/', catalog.views.cloth_view, name='cloth'),
    path('sport/', catalog.views.sport_view, name='sport'),
    path('petrol/', catalog.views.petrol_view, name='petrol'),
    path('service/', catalog.views.service_view, name='service'),
    path('home/', catalog.views.home_view, name='home'),
    path('leisure/', catalog.views.leisure_view, name='leisure'),
    path('mobile/', catalog.views.mobile_view, name='mobile'),
    path('internet/', catalog.views.internet_view, name='internet'),
]