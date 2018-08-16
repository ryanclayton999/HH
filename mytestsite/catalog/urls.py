from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('findus/', views.find_us, name = 'Find Us'),
	path('food/', views.food, name = 'Food'),
	path('icecream/', views.icecream, name = 'icecream'),
]