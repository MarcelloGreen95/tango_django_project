from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.sites.urls),
]
