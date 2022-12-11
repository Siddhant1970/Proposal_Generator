
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('submitt_form',views.submitt_form, name='submitt_form'),
    path('main',views.main),
    path('login_submit',views.login_submitt),
    path('logout',views.logout),
    path('contact',views.contact_form),
    path('generate_prop',views.generate_prop),
    path('proposals',views.proposals),
    path('prac',views.prac),
    path('proposalDetails3/<proposal_id>', views.proposalDetails3, name='proposalDetails3'),
    path('proposalDetails3/final3/', views.final3, name='final3'),
    # path('',views.adminpage3,name="adminhome3")
]
