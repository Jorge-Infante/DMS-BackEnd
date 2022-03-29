"""DMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from applications.users.urls import router_user
from applications.movies.urls import router_movie
schema_view = get_schema_view(
   openapi.Info(
      title="API-DRUD MOVIE STORE",
      default_version='v1',
      description="Documentación de la api DRUP MOVIE STORE",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jainfante@unicesar.edu.co"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/',include('applications.users.urls')),
    path('api/',include('applications.movies.urls')),
    path('api/',include(router_user.urls)),
    path('api/',include(router_movie.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
