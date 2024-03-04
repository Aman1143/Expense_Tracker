from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
import json
# Create your models here.


class UserProfile(models.Model): 
    name=models.CharField(max_length=20)
    email=models.EmailField()
    current_buget = models.DecimalField(max_digits=20, decimal_places=2)
    total_buget = models.DecimalField(max_digits=20, decimal_places=2)
    password=models.CharField(max_length=128)
    def save(self, *args, **kwargs): 
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Expenses(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    expenses_info = models.TextField(default="[]")

    def add_expense(self,string_info,amount_info,date_info):
        expense_list=json.loads(self.expenses_info)
        
        expense_list.append({
			"string_info":string_info,
             "amount_info":amount_info,
             "date_info":date_info
		})

    def remove_expense(self, index):
        expense_list = json.loads(self.expenses_info)
        del expense_list[index]
        self.expenses_info = json.dumps(expense_list)
        self.save()

    def get_expense_list(self):
        return json.loads(self.expenses_info)


class Savings(models.Model): 
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    saving_info = models.TextField(default="[]")

    def add_saving(self, string_info, amount_info, date_info):
        saving_list = json.loads(self.saving_info)
        saving_list.append({
            "string_info": string_info,
            "amount_info": amount_info,
            "date_info": date_info,
        })
