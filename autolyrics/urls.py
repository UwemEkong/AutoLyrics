from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

urlpatterns+= staticfiles_urlpatterns()


# Use include() to add paths from the app application 
from django.urls import include
from django.urls import path

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='home/', permanent=True)),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
