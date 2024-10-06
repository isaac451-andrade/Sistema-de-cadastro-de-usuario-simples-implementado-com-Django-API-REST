from django.contrib import admin
from django.urls import path, include
from homePage import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
    path('', views.home, name='homePage')
]
