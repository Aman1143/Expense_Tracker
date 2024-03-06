from django.db import models
from django.contrib.auth.hashers import make_password
import json


class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    current_buget = models.DecimalField(max_digits=20, decimal_places=2)
    total_buget = models.DecimalField(max_digits=20, decimal_places=2)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone
import json

class Expenses(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    expenses_info = models.TextField(default="[]")

    def add_expense(self, string_info, amount_info, date_info):
        expense_list = json.loads(self.expenses_info)

        expense_list.append({
            "string_info": string_info,
            "amount_info": amount_info,
            "date_info": date_info
        })

        self.expenses_info = json.dumps(expense_list)   
        self.save()  

    def remove_expense(self, index):
        expense_list = json.loads(self.expenses_info)
        del expense_list[index]
        self.expenses_info = json.dumps(expense_list)
        self.save()

    def get_expense_list(self):
        return json.loads(self.expenses_info)



class Savings(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    savings_info = models.TextField(default="[]")

    def add_savings(self, string_info, amount_info, date_info):
        savings_list = json.loads(self.savings_info)

        savings_list.append({
            "string_info": string_info,
            "amount_info": amount_info,
            "date_info": date_info
        })

        self.savings_info = json.dumps(savings_list)   
        self.save()   

    def remove_savings(self, index):
        savings_list = json.loads(self.savings_info)
        del savings_list[index]
        self.savings_info = json.dumps(savings_list)
        self.save()

    def get_expense_list(self):
        return json.loads(self.savings_info)
