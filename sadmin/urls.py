from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminpage2,name="adminhome2"),
    path('proposalDetails2/<proposal_id>', views.proposalDetails2, name='proposalDetails2'),
    path('proposalDetails2/final/', views.final, name='final'),
]