from django import forms 
from .models import Category, Budget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['products', 'lanches', 'cloth', 'sport', 'petrol', 'service', 'home', 'leisure', 'mobile', 'internet']
        
class BudgetForm(forms.ModelForm);
    class Meta:
        model = Budget
        fields = ['id', 'amount', 'period_start', 'period_end', 'category']
