
from django.contrib import admin
from django.urls import path,include
from .views import Home_View
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('Account.urls')),
    path('',Home_View)
]
