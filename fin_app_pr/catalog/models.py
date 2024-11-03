from django.db import models
from django.db.models import SmallAutoField, CharField, ForeignKey, DecimalField, TextField, DateField
from django.utils import timezone   
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    products = DecimalField(max_digits=19, decimal_places=10, default=0)
    lunches = DecimalField(max_digits=19, decimal_places=10, default=0)
    cloth = DecimalField(max_digits=19, decimal_places=10, default=0)
    sport = DecimalField(max_digits=19, decimal_places=10, default=0)
    petrol= DecimalField(max_digits=19, decimal_places=10, default=0)
    service = DecimalField(max_digits=19, decimal_places=10, default=0)
    home = DecimalField(max_digits=19, decimal_places=10, default=0)
    leisure = DecimalField(max_digits=19, decimal_places=10, default=0)
    mobile = DecimalField(max_digits=19, decimal_places=10, default=0)
    internet = DecimalField(max_digits=19, decimal_places=10, default=0)
    
    class Meta:
        db_table = 'categories'
        
    def total_expenses(self):
        return (self.products + self.lunch + self.cloth + 
                self.sport + self.petrol + self.service + 
                self.home + self.leisure + self.mobile + 
                self.internet)
    
    def __repr__(self):
        return (f'{self.id}\n'
               f'{self.name}\n'
               f'{self.products}\n'
               f'{self.lunch}\n'
               f'{self.cloth}\n'
               f'{self.sport}\n'
               f'{self.petrol}\n'
               f'{self.service}\n'
               f'{self.home}\n'
               f'{self.leisure}\n'
               f'{self.mobile}\n'
               f'{self.internet}')
               
class Budget(models.Model):
    id = SmallAutoField(primary_key=True)
    amount = DecimalField(max_digits=19, decimal_places=10, default=0)
    period_start = models.DateField(default=timezone.now)
    period_end = models.DateField(default=timezone.now)
    category = ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'budgets'
        
    def __repr__(self):
        return (f'{self.id}\n'
               f'{self.amount}\n'
               f'{self.period_start}\n'
               f'{self.period_end}\n'
               f'{self.category}\n')
               

    
