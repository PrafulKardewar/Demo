from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Product API Set Of Operations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/',include('appone.urls')),
    path('api-auth/', include('rest_framework.urls')),#http://localhost:8000/api-auth/
    url(r'swagger/', schema_view) #http://localhost:8000/swagger
]
