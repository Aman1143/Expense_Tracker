from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile,Expenses,Savings
from django.contrib.auth.hashers import check_password 
from django.utils import timezone
import json
import jwt 
from . import  prediction
 


@api_view(['POST'])
def resgister(request):
    if request.method == "POST": 
        data = json.loads(request.body)   
        email=data['email']
        password=data['password']
        name=data['name'] 
        
        try:
            user_profile = UserProfile.objects.get(email=email)
            return Response({'success': False, 'message': 'User already exists'})
        except UserProfile.DoesNotExist:
            pass
        
        user_profile = UserProfile.objects.create(name=name, email=email, current_buget=0, total_buget=0, password=password)
        print("User created")
        payload = {
            'user_id': user_profile.id,
            'email': email,
            'name': name 
        }
        secret_key = "asdsknd"
        
        try:
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            return Response({"success": True, 'token': token.encode('utf-8')})
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
    data = json.loads(request.body)  
    string_info = data['label']
    amount_info = data['number']
    date_info = timezone.now().date().isoformat()  
    user = UserProfile.objects.get(id=request.id)  
    try: 
        expense_instance = Expenses.objects.get(user=user)
        expense_instance.add_expense(string_info, amount_info, date_info) 
        return Response({"success": True, "message": "done"})
    except Expenses.DoesNotExist:
        expense_instance = Expenses.objects.create(user=user) 
        expense_instance.add_expense(string_info, amount_info, date_info) 
        return Response({"success": True, "message": "done"})

         
        
        
        
        
        
@api_view(['GET'])
def getExpense(request):
    user=UserProfile.objects.get(id=request.id) 
    
    expense_list=Expenses.objects.get(user=user)   
    
    return Response({'data':expense_list.expenses_info,"success":True})


@api_view(['POST'])
def getPredictionOutput(request):
     try:    
            data = json.loads(request.body)   
            predict = prediction.helper(data['sentance']) 
            if isinstance(predict, (dict, list, str, int, float)):
                print(predict)
                return Response({'predict':predict,"success":True})
            else: 
                return Response({'error': 'Object returned by prediction is not JSON serializable.'})

     except Exception as error:
         return Response({'error': "error"})