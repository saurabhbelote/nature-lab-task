from django.urls import path
from .views import RegisterView, LoginView, Userview, Logout




app_name = 'authentication'
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('userdetails/', Userview.as_view(), name='details'),
    path('logout/', Logout.as_view(), name='logout'),

]
