from django.urls import path
from . import views

app_name = 'saju'
urlpatterns = [
    path('', views.input_view, name='input'),
    path('result/', views.result_view, name='result'),

]