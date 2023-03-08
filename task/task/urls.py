from django.contrib import admin
from django.urls import path, include
from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('api/',include('api.urls')),
    path("",index,name="index"),
]
