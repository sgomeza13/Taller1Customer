from django.urls import path 
from .views import CustomerHomeView, RegisterView, CustomerListView, CustomerView, CreatedCustomerView, error, LoginView

urlpatterns = [
    path("",CustomerHomeView.as_view(),name='home'),
    path('register/',RegisterView.as_view(),name='register'),
    path('list/',CustomerListView.as_view(),name='list'),
    path('list/<str:id>',CustomerView.as_view(),name='customer'),
    path('register/created/<str:email>',CreatedCustomerView.as_view(),name='created'),
    path('login/',LoginView.as_view(),name='login'),
    path("error/",error.as_view(),name='error'),

]