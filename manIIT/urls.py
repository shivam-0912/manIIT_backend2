"""manIIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
      title="manIIT API",
      default_version='v1',
      description="Your description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
            path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('',schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('user/',include('user.urls')),#connecting to url file of app 
    path('club/',include('club.urls')),#connecting to url file of app 
    path('post/',include('post.urls')),#connecting to url file of app 
    path('admin/', admin.site.urls),
]
