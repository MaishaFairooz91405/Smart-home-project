from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This connects your app's URLs to the /api/ prefix
    path('api/', include('apps.product.urls')),
    path('user/', include('apps.user.urls')),
    path("api/", include("inventory.urls")),
    path("api/", include("room.urls"))

]
