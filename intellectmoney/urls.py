from django.urls import path

from intellectmoney import views

urlpatterns = [
    path('result/', views.receive_result, name='intellectmoney-result'),
    path('success/result/', views.success, name='intellectmoney-success'),
    path('fail/result/', views.fail, name='intellectmoney-fail'),
]
