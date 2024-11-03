from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from . import models
from .models import Budget, Category



"""Главная страница"""
def main(request):
    return render(request,'index.html')
    
"""Страница категорий"""
def categories(request):
    return render(request, 'categories.html')
    
"""Страница бюджета"""   
def budgets(request):
    budgets = Budget.objects.all()
    categories = Category.objects.all
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        category_id = request.POST.get('category_id')
        period_start = request.POST.get('period_start')
        period_end = request.POST.get('period_end')
        
        if amount and category_id:
            try:
                budget = Budget(
                amount = float(amount),
                period_start = period_start,
                period_end = period_end,
                category_id = category_id
                )
                budget.save()
            except ValueError:
                pass
                
        return redirect('budgets')
                
    return render(request, 'budgets.html', {'budgets': budgets, 'categories': categories})
    
def products_view(request):
    return render(request, 'products.html')

def lunches_view(request):
    return render(request, 'lunches.html')
    
def cloth_view(request):
    return render(request, 'cloth.html')
    
def sport_view(request):
    return render(request, 'sport.html')
    
def petrol_view(request):
    return render(request, 'petrol.html')
    
def service_view(request):
    return render(request, 'service.html')
    
def home_view(request):
    return render(request, 'home.html')

def leisure_view(request):
    return render(request, 'leisure.html')
    
def mobile_view(request):
    return render(request, 'mobile.html')

def internet_view(request):
    return render(request, 'internet.html')
    
