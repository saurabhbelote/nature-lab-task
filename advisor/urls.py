from django.urls import path
from . import views
app_name = 'advisor'


urlpatterns = [

    path('user/<str:email>/advisor',views.advisor_list.as_view({'create': 'list'}) , name = 'advisor_list'),
    path('user/<str:email>/advisor/<int:advisor_id>',views.advisor_book.as_view({'create': 'list'}) , name = 'advisor_book'),
    path('user/<str:email>/advisor/booking',views.booking_list.as_view({'get': 'list'}) , name = 'booking_list'),
    path('base',views.base.as_view() , name = 'base'),
    path('AdvisorView',views.AdvisorBookView.as_view() , name = 'AdvisorView'),
    path('user/<str:email>/advisor/<int:advisor_id>',views.AdvisorCreateView.as_view() , name = 'AdvisorCreateView'),
    path('',views.AdvisorView.as_view() , name = 'AdvisorView'),

]
