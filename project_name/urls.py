"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from main.urls import apiurls as main_apiurls


# Create the API namespace and add the API only URLs of the applications
apiurls = ([
    path('main/', include(main_apiurls, namespace='main')),
], 'api')

urlpatterns = [
    path('', include('main.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include(apiurls, namespace='api')),
    path('admin/', admin.site.urls),
]

if hasattr(settings, 'DEBUG_TOOLBAR') and settings.DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]


if not settings.IS_PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
