from django.urls import path
from donation import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('Donor',views.DonorPage.as_view(),name='DonorPage'),
]