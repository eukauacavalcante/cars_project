from django.urls import path

from .views import (CarDeleteView, CarDetailView, CarListView, CarUpdateView,
                    NewCarCreateView)

urlpatterns = [
    path('', CarListView.as_view(), name='cars_list'),
    path('novo-carro/', NewCarCreateView.as_view(), name='new_cars_list'),
    path('carro/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('carro/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('carro/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]