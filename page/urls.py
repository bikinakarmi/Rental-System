from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home.as_view(), name='home'),
    path('login',auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup',views.signup, name='signup'),
    path('logout',auth_views.LogoutView.as_view(), name='logout'),
    path('create',views.PropertyCreateView.as_view(), name='create_property'),   
    path('property/<int:pk>',views.PropertyDetailView.as_view(),name = 'property_view'),
    path('property/edit/<int:pk>',views.PropertyUpdateView.as_view(),name = 'property_edit'),
    path('property/delete/<int:pk>',views.PropertyDeleteView,name = 'property_delete'),



]