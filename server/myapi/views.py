from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile,Expenses,Savings
from django.contrib.auth.hashers import check_password 
from django.utils import timezone
import json
import jwt 

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hellooo world!'})


@api_view(['POST'])
def resgister(request):
    if request.method == "POST": 
        data = json.loads(request.body)  
        email=data['email']
        password=data['password']
        name=data['name'] 
        
        
        if UserProfile.objects.get(email=email).exists():  
            return Response({'succes': False})
        
        UserProfile.objects.create(name=name,email=email,current_buget=0,total_buget=0,password=password) 
        user=UserProfile.objects.get(email=email)
        payload = {
            'user_id': user.id,
            'email': email,
            'name': name 
        }
        secret_key="asdsknd"
        
        
        try:
            token=jwt.encode(payload,secret_key,algorithm='HS256')
            return Response({"success":True,'token':token.encode('utf-8')})
        except Exception as e:
            return Response({'success': False, 'message': 'Failed to generate token'}, status=500)


@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    email = data['email']
    password = data['password']
    
    try:
        user = UserProfile.objects.get(email=email)  
    except UserProfile.DoesNotExist:
        return Response({"success": False, "message": "User does not exist"})
    
    if check_password(password,user.password):   
        user=UserProfile.objects.get(email=email)
        payload = {
                'user_id': user.id,
                'email': email,
                'name': user.name 
        }
        secret_key="asdsknd"
            
            
        try:
            token=jwt.encode(payload,secret_key,algorithm='HS256')
            return Response({"success":True,'token':token.encode('utf-8')})
        except Exception as e:
            return Response({'success': False, 'message': 'Failed to generate token'}, status=500)
    else:
        return Response({'success': False, 'message': 'password not match'})

@api_view(['POST'])
def prompt(request): 
     
    data=json.loads(request.body) 
    string_info=data['label']
    amount_info=data['number']
    date_info = timezone.now().date()
    user=UserProfile.objects.get(id=request.id) 
    expense_instance=Expenses.objects.create(user_id=user) 
    expense_instance.add_expense(string_info,amount_info,date_info)
    print(expense_instance.get_expense_list)
    return Response({"message": "done"})

@api_view(['GET'])
def getExpense(request):
    user=UserProfile.objects.get(id=request.id) 
    all_expenses = Expenses.objects.all()

    for expense in all_expenses:
        expense_list = expense.get_expense_list()
        for item in expense_list:
            string_info = item['string_info']
            amount_info = item['amount_info']
            date_info = item['date_info']
            print(string_info, amount_info, date_info)
    
    expense_list=Expenses.objects.get(user_id=user)
    print("sdfs")
    print(expense_list.expenses_info)
    
    return Response({'data':expense_list.expenses_info})