from django.urls import path 
from .views import CustomerHomeView, RegisterView, CustomerListView, CustomerView, CreatedCustomer

urlpatterns = [
    path("",CustomerHomeView.as_view(),name='home'),
    path('register/',RegisterView.as_view(),name='register'),
    path('list/',CustomerListView.as_view(),name='list'),
    path('list/<str:id>',CustomerView.as_view(),name='customer'),
    path('register/created/<str:email>',CreatedCustomer.as_view(),name='created'),
]