from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Task Management API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page for the API
    path('api/tasks/', include('tasks.urls')),  # Include tasks app URLs
    path('auth/', include('rest_authtoken.urls')),  # Auth token URLs
]
