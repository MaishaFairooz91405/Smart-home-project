from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # This connects your app's URLs to the /api/ prefix
    path('api/', include('apps.product.urls')),
    path('user/', include('apps.user.urls')),
    path("api/", include("inventory.urls")),
    path("api/", include("room.urls"))


]
