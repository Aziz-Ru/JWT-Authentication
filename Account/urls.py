from django.urls import path
from .views import *
urlpatterns =[
    path('register/', Register_View.as_view()),
    path('login/', Login_View.as_view()),
    # path('verify/', Verify_Account_View.as_view()),
    path('profile/', Profile_View.as_view()),
    path('change_password/', Change_Password_View.as_view()),
    path('password_reset/<uid>/<token>/', Login_View.as_view()),
]