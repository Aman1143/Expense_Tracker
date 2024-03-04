from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('resgister/', csrf_exempt(views.resgister), name="resgister"),
    path('login/',csrf_exempt(views.login),name="login"),
    path('prompt/',csrf_exempt(views.prompt),name="prompt"),
    path('getExpense/',views.getExpense,name="getExpense")
]
