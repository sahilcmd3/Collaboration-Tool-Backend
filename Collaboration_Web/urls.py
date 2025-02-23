from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Collab import views
from django.views.generic import RedirectView

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'files', views.FileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/', permanent=True)),  # Add this line to redirect the root URL
]