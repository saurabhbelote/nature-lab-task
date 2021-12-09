from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
#from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from advisor.views import advisor_list, booking_list,advisor_book,ProfileDetail
from .  import settings



router = routers.DefaultRouter()
router.register('advisor/email', advisor_list)
router.register('user/booking/<int:id>', booking_list, basename='list')
router.register('booking', advisor_book)




urlpatterns = [
    path('routers',include(router.urls),name ='routers'),
    path('api', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('',include('authentication.urls')),
    path('advisor',include('advisor.urls'),name = 'adv_app'),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

