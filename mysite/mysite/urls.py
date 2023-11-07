

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('admin/', admin.site.urls),
    path('reg/', include('reg.urls')),
    path('reg/', include('django.contrib.auth.urls')),
]
