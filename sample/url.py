from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('brian/', views.brian, name='brian'), 
    path('enock/', views.enock, name='enock'), 
    path('<str:name>/', views.greet, name='greet')
]