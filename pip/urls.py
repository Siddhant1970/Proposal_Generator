from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminpage,name='adminhome'),
    path('proposalDetails2/<proposal_id>', views.proposalDetails, name='proposalDetails'),
    path('proposalDetails2/final/', views.final, name='final'),
]