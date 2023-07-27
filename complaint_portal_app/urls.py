
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('Customer/', views.newCustomer, name='newCustomer'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('complain/', views.complain, name='complain'),
    path('otp_verification/<str:username>/',
         views.otp_verification, name="otp_verification"),
    path('customer_history/<int:id>',views.customer_history,name="customer_history"),
    # path(r'^', views.redirectuser, name='redirectuser'),
    path('logout/', views.logout_user,name="logout"),
    path('complain_form/', views.complain_form, name='complain_form'),

    path('view_logs/<str:id>',views.view_logs,name="view_logs"),
    ############## OE path #################
    # path('OE/', views.Operation_executive, name='OE'),
    path('OE_login/', views.OE_login, name="OE_login"),
    path('All_complaints/', views.All_complaints, name="All_complaints"),
    path('track_status/<int:id>',
         views.track_status, name="track_status"),
    path('update_complaint_status/<int:id>',
         views.update_complaint_status, name="update_complaint_status"),
    path('complaint_feedback/',views.complaint_feedback,name="complaint_feedback"),
]
