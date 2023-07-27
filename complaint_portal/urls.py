
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
# from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from . import settings
# from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('oauth/', include('social_django.urls', namespace='social')),

    # path('accounts/', include('allauth.urls')),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    # path('', TemplateView.as_view(template_name="home.html")),
    # path(r'^', include('complaint_portal_app.urls')),
    path('', include('complaint_portal_app.urls')),



] 
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
